# Task Schema
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date = datetime
    assigne_id = Optional[int] = None # Optional FK to User.
    # We’re excluding project_id from TaskCreate, since it will be passed in the route (e.g. /projects/{project_id}/tasks/)

# Input
class TaskCreate(TaskBase):
    pass

# Output
class TaskRead(TaskBase):
    id: int
    project_id: int
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
