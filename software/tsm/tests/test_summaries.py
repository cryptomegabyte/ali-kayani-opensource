import json

import pytest


def test_create_summary(test_app_with_db) -> None:
    """
    Tests the /summaries/ default route
    """

    "Given: test_app_with_db"

    # when
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://test.url"})
    )

    # then
    assert response.status_code == 201
    assert response.json()["url"] == "https://test.url"


def test_create_summaries_invalid_json(test_app):
    """
    Tests the /summaries/ route for an exception
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
