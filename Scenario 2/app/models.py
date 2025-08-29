from enum import Enum
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone, date

# POST /tasks shows TaskCreate
# PUT /tasks/{id} might show TaskUpdate
# GET /tasks returns TaskRead

# Enums
class TaskStatus(str, Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

# Shared Fields
class TaskBase(SQLModel):
    title: str
    description: str | None = None # Optional
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    due_date: date | None = None # Optional

# Input Task Class
class TaskCreate(TaskBase):
    pass

# DataBase Model
class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # default_factory ensures the time is fresh every time a new task is created.
    created_at: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))

# Output Task Model
class TaskRead(TaskBase):
    id: int
    created_at: datetime