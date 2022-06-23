import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    """
    Defines a settings class with two atrributes
    """
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)

@lru_cache
def get_settings() -> BaseSettings:
    """
    Returns the settings
      Input: None
      Return: BaseSettings Class
    """
    log.info("Loading config settings from the environment.....")
    return Settings()