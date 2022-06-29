import json

import pytest

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


def test_read_all_summaries(test_app_with_db):
    """
    Tests the  /summaries post default route to read all summaries
    """

    "Given: test_app_with_db"

    response = test_app_with_db.post("/summaries/", data=json.dumps(url))
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1
