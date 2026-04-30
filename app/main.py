from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging, request_context_middleware


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title=settings.app_name, version=settings.version)
    app.middleware("http")(request_context_middleware)
    app.include_router(api_router)
    return app


app = create_app()
