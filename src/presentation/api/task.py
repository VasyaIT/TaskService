from typing import Sequence
from uuid import UUID

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from src.database.exceptions import NotFoundError
from src.dependencies.repository import TaskRepositoryDep
from src.dto.task import CreateTaskDTO, TaskDTO
from src.models.task import Task
from src.presentation.const import TaskStatus


task_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@task_router.post("")
async def create_task(dto: CreateTaskDTO, repository: TaskRepositoryDep) -> TaskDTO:
    """Create task"""
    return await repository.create(dto)


@task_router.get("", response_model=list[TaskDTO])
async def get_all_tasks(
    repository: TaskRepositoryDep, filter_by: TaskStatus = TaskStatus.AVAILABLE
) -> Sequence[Task]:
    """Get all tasks with filter by task status"""
    return await repository.get_many(status=filter_by)


@task_router.put("/{task_id}")
async def edit_task(task_id: UUID, dto: CreateTaskDTO, repository: TaskRepositoryDep) -> TaskDTO:
    """Edit task by id"""
    try:
        return await repository.update(task_id, dto)
    except NotFoundError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@task_router.delete("/{task_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID, repository: TaskRepositoryDep) -> None:
    """Delete task by id"""
    try:
        await repository.delete(task_id)
    except NotFoundError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
