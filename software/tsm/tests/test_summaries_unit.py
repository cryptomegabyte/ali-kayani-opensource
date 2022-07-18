import json
from datetime import datetime

import pytest
from app.api import crud, summaries
from app.models.pydantic import SummaryPayloadSchema


def test_mocked_create_summary(test_app, monkeypatch) -> None:
    """
    Tests the /summaries/ post default route
    """

    "Given: test_app"

    test_request_payload = {"url": "https://foo.bar"}
    test_response_payload = {"id": 1, "url": "https://foo.bar"}

    async def mock_post(payload: SummaryPayloadSchema) -> int:
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    # when
    response = test_app.post("/summaries/", data=json.dumps(test_request_payload))

    # then
    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_summaries_invalid_json(test_app) -> None:
    """
    Tests the /summaries/ post route for an exception
    """

    "Given: test_app"

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


def test_mocked_read_summary(test_app, monkeypatch) -> None:
    """
    Tests the get /summaries/ default route with incorrect id
    """

    "Given: test_app"

    test_data = {
        "id": 1,
        "url": "https://foo.bar",
        "summary": "summary",
        "created_at": datetime.utcnow().isoformat(),
    }

    async def mock_get(id: int) -> dict:
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    # when
    response = test_app.get("/summaries/1/")

    # then
    assert response.status_code == 200
    assert response.json() == test_data


def test_mocked_read_summary_incorrect_id(test_app, monkeypatch) -> None:
    """
    Tests the  /summaries delete route with incorrect id
    """

    "Given: test_app"

    async def mock_get(id: int) -> None:
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    # when
    response = test_app.get("/summaries/999/")

    # then
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_mock_read_all_summaries(test_app, monkeypatch) -> None:
    """
    Tests the  /summaries post default route to read all summaries
    """

    "Given: test_app"

    test_data = [
        {
            "id": 1,
            "url": "https://foo.bar",
            "summary": "summary",
            "created_at": datetime.utcnow().isoformat(),
        },
        {
            "id": 2,
            "url": "https://testdrivenn.io",
            "summary": "summary",
            "created_at": datetime.utcnow().isoformat(),
        },
    ]

    async def mock_get_all() -> dict:
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    # when
    response = test_app.get("/summaries/")

    # then
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_summary(test_app, monkeypatch):
    pass


def test_remove_summary_incorrect_id(test_app, monkeypatch):
    pass


def test_update_summary(test_app, monkeypatch):
    pass


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
    test_app, monkeypatch, summary_id, payload, status_code, detail
):
    pass


def test_update_summary_invalid_url(test_app):
    response = test_app.put(
        "/summaries/1/",
        data=json.dumps({"url": "invalid", "summary": "updated!"}),
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "invalid or missing URL scheme"
