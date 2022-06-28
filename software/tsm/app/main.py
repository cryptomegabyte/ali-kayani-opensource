# imports
from os import environ

from app.api import ping
from app.config import Settings, get_settings
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

# Main app
app = FastAPI()

# Creates the application
def create_application() -> FastAPI:
    application = FastAPI()

    register_tortoise(
        application,
        db_url=environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

    application.include_router(ping.router)

    return application


app = create_application()
