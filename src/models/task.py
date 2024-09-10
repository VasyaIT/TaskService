from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.presentation.const import TaskPriority, TaskStatus


class Task(Base):
    title: Mapped[str] = mapped_column(String)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority))
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.AVAILABLE)
