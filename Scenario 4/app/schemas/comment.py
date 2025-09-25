# Comment Schemas
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Shared base
class CommentBase(BaseModel):
    comment: str


# Input 
class CommentCreate(CommentBase):
    author_id: int


# Output
class CommentRead(CommentBase):
    id: int
    author_id: int
    task_id: int
    created_at: datetime

    class Config:
        from_attributes = True
