import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """
    Defines a settings class with three atrributes
     - Environment which defaults to dev
     - Testing Boolean which defaults to 0
     - Postgres db url
    """

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> BaseSettings:
    """
    Returns the settings
      Input: None
      Return: BaseSettings Class
    """
    log.info("Loading config settings from the environment.....")
    return Settings()
