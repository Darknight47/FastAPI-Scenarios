# Project Schema
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Base
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    due_date: datetime


# Input schema
class ProjectCreate(ProjectBase):
    pass


# Output schema
class ProjectRead(ProjectBase):
    id: int
    team_id: int
    created_at: datetime
    update_at: datetime

    class Config:
        from_attributes = True