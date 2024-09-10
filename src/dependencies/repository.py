from typing import Annotated, Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.session import db_session
from src.repositories.base import BaseRepository
from src.repositories.task import TaskRepository


def get_repository(repo_type: type[BaseRepository]) -> Callable[[AsyncSession], BaseRepository]:
    def _get_repo(async_session: AsyncSession = Depends(db_session)) -> BaseRepository:
        return repo_type(async_session=async_session)
    return _get_repo


TaskRepositoryDep = Annotated[TaskRepository, Depends(get_repository(TaskRepository))]
