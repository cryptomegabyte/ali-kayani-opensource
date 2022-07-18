import json

import pytest

# =====POST Route Tests=====

# Define the test url
url = {"url": "https://test.url"}


def test_create_summary(test_app_with_db) -> None:
    """
    Tests the /summaries/ post default route
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.post("/summaries/", data=json.dumps(url))

    # then
    assert response.status_code == 201
    assert response.json()["url"] == url["url"]


def test_create_summaries_invalid_json(test_app) -> None:
    """
    Tests the /summaries/ post route for an exception
    """

    "Given: test_app_with_db"

    # when
    response = test_app.post("/summaries/", data=json.dumps({}))

    # then
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }

    # when
    response = test_app.post("/summaries/", data=json.dumps({"url": "invalid://url"}))

    # then
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "URL scheme not permitted"


def test_read_summary(test_app_with_db) -> None:
    """
    Tests the read /summaries/ post route
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.post("/summaries/", data=json.dumps(url))

    summary_id = response.json()["id"]
    response = test_app_with_db.get(f"/summaries/{summary_id}")

    # then
    assert response.status_code == 200

    # when
    response_dict = response.json()

    # then
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == url["url"]
    assert response_dict["summary"]
    assert response_dict["created_at"]


# =====GET Route Tests=====


def test_read_summary_incorrect_id(test_app_with_db):
    """
    Tests the get /summaries/ default route with incorrect id
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.get("/summaries/999/")

    # then
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"

    # when
    response = test_app_with_db.get("/summaries/0/")

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "id"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error.number.not_gt",
                "ctx": {"limit_value": 0},
            }
        ]
    }


def test_read_all_summaries(test_app_with_db):
    """
    Tests the  /summaries post default route to read all summaries
    """

    "Given: test_app_with_db"

    response = test_app_with_db.post("/summaries/", data=json.dumps(url))
    summary_id = response.json()["id"]

    # when
    response = test_app_with_db.get("/summaries/")

    # then
    assert response.status_code == 200

    # when
    response_list = response.json()

    # then
    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1


# =====DELETE Route Tests=====


def test_remove_summary(test_app_with_db):
    """
    Tests the  /summaries delete route
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.post("/summaries/", data=json.dumps(url))
    summary_id = response.json()["id"]

    response = test_app_with_db.delete(f"/summaries/{summary_id}/")

    # then
    assert response.status_code == 200
    assert response.json() == {"id": summary_id, "url": url["url"]}


def test_remove_summary_incorrect_id(test_app_with_db):
    """
    Tests the  /summaries delete route with incorrect id
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.delete("/summaries/999/")

    # then
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"

    # when
    response = test_app_with_db.delete("/summaries/0/")

    # then
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "id"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error.number.not_gt",
                "ctx": {"limit_value": 0},
            }
        ]
    }


# =====PUT Route Tests=====

summary_data = {**url, "summary": "updated!"}


def test_update_summary(test_app_with_db):
    """
    Tests the  /summaries PUT route
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.post("/summaries/", data=json.dumps(url))
    summary_id = response.json()["id"]

    response = test_app_with_db.put(
        f"/summaries/{summary_id}/", data=json.dumps(summary_data)
    )

    # then
    assert response.status_code == 200

    # when
    response_dict = response.json()

    # then
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == url["url"]
    assert response_dict["summary"] == "updated!"
    assert response_dict["created_at"]


@pytest.mark.parametrize(
    "summary_id, payload, status_code, detail",
    [
        [
            999,
            {"url": "https://foo.bar", "summary": "updated!"},
            404,
            "Summary not found",
        ],
        [
            0,
            {"url": "https://foo.bar", "summary": "updated!"},
            422,
            [
                {
                    "loc": ["path", "id"],
                    "msg": "ensure this value is greater than 0",
                    "type": "value_error.number.not_gt",
                    "ctx": {"limit_value": 0},
                }
            ],
        ],
        [
            1,
            {},
            422,
            [
                {
                    "loc": ["body", "url"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "summary"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ],
        ],
        [
            1,
            {"url": "https://foo.bar"},
            422,
            [
                {
                    "loc": ["body", "summary"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ],
        ],
    ],
)
def test_update_summary_invalid(
    test_app_with_db, summary_id, payload, status_code, detail
):
    """
    Tests the  /summaries PUT route with invalid data
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.put(
        f"/summaries/{summary_id}/", data=json.dumps(payload)
    )

    # then
    assert response.status_code == status_code
    assert response.json()["detail"] == detail


def test_update_summary_invalid_url(test_app):
    """
    Tests the  /summaries PUT route with invalid url
    """

    "Given: test_app_with_db"
    response = test_app.put(
        "/summaries/1/", data=json.dumps({"url": "invalid", "summary": "updated!"})
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "invalid or missing URL scheme"
