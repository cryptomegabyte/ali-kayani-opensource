
#imports
from fastapi import FastAPI, Depends
from app.config import Settings, get_settings

# Main app
app = FastAPI()

@app.get("/ping")
async def pong(
    settings: Settings = Depends(get_settings)
) -> None:
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }