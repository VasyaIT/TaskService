from enum import Enum


class TaskStatus(Enum):
    AVAILABLE = "available"
    STARTED = "started"
    FINISHED = "finished"


class TaskPriority(Enum):
    LOW = "low"
    MIDDLE = "middle"
    HIGH = "high"
