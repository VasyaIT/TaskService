from fastapi import APIRouter

from src.presentation.api.task import task_router


def get_base_router() -> APIRouter:
    base_router = APIRouter(prefix="/api")
    base_router.include_router(task_router)
    return base_router
