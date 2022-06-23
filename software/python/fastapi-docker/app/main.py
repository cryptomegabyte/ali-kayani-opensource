
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def pong() -> None:
    return {
        "ping": "pong!"
    }