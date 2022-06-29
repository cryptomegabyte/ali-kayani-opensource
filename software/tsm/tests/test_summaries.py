import json

import pytest


def test_create_summary(test_app_with_db) -> None:
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://test.url"})
    )

    assert response.status_code == 201
    assert response.json()["url"] == "https://test.url"
