from uuid import UUID

from src.dto.base import BaseDTO
from src.presentation.const import TaskPriority, TaskStatus


class CreateTaskDTO(BaseDTO):
    title: str
    priority: TaskPriority
    status: TaskStatus = TaskStatus.AVAILABLE


class TaskDTO(CreateTaskDTO):
    id: UUID
