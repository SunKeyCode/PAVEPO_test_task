from fastapi import FastAPI

from api import main_router
from settings.config import AppSettings


def create_app():
    app = FastAPI()
    app.include_router(main_router)

    return app
