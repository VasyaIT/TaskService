from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.config_app import settings
from src.presentation.routers import get_base_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.TITLE_APP)
    app.include_router(get_base_router())
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"],
        allow_headers=["*"],
        allow_credentials=True
    )
    return app


app = create_app()
