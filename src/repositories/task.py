from typing import Sequence

from sqlalchemy import Result, select, update, insert, delete

from src.dto.task import CreateTaskDTO, TaskDTO
from src.models.task import Task
from src.database.exceptions import NotFoundError
from src.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    async def get_one(self, task_id: int) -> TaskDTO:
        stmt = select(Task).filter_by(id=task_id)
        result = await self.session.execute(stmt)
        return self._get_result(result, task_id)

    async def get_many(self, **filters) -> Sequence[Task]:
        stmt = select(Task).filter_by(**filters)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, dto: CreateTaskDTO) -> TaskDTO:
        stmt = insert(Task).values(dto.model_dump()).returning(Task)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self._get_result(result)

    async def update(self, task_id, dto: CreateTaskDTO) -> TaskDTO:
        stmt = update(Task).values(dto.model_dump()).filter_by(id=task_id).returning(Task)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self._get_result(result, task_id)

    async def delete(self, task_id) -> TaskDTO:
        stmt = delete(Task).filter_by(id=task_id).returning(Task)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self._get_result(result, task_id)

    def _get_result(self, result: Result, task_id: int | None = None) -> TaskDTO:
        task = result.scalar_one_or_none()
        if not task:
            raise NotFoundError(f"Task with id: {task_id} not found")
        return TaskDTO(**task.__dict__)
