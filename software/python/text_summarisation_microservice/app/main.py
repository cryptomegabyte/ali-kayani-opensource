
#imports
from os import environ
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from app.config import Settings, get_settings

# Main app
app = FastAPI()

register_tortoise(
    app,
    db_url=environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=False,
    add_exception_handlers=True
)

#Example route
# [TODO] - Refactor using fastapi router
@app.get("/ping")
async def pong(
    settings: Settings = Depends(get_settings)
) -> None:
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }