#imports
from os import environ
import pytest
from starlette.testclient import TestClient # Uses the underlying starlette library test client

from app import main
from app.config import get_settings, Settings

def get_settings_override() -> None:
    """
    Overrides the settings
    """
    return Settings (
        testing=1, 
        database_url=environ.get("DATABASE_TEST_URL")
    )

@pytest.fixture(scope="module")
def test_app() -> None:
    
    # Set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    #tear down
