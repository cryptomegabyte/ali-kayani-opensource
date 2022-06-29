# imports
import logging

from app.api import ping, summaries
from app.db import init_db
from fastapi import FastAPI

# start the logger
log = logging.getLogger("uvicorn")

# Main app
app = FastAPI()


def create_application() -> FastAPI:
    """
    Creates the application
    Input: None
    Returns: FastAPI application
    """
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


# Initialises the app
app = create_application()

# Startup event handler
@app.on_event("startup")
async def startup_event() -> None:
    log.info("Starting up...")
    init_db(app)


# Shutdown event handler
@app.on_event("shutdown")
async def shutdown_event() -> None:
    log.info("Shutting down...")
    init_db(app)
