# Schema for feedback
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FeedbackCreate(BaseModel):
    challenge_id: int
    rating: Optional[int] = Field(None, ge=1, le=5, description="Rating between 1 and 5")
    comment: Optional[str] = Field(None, max_length=500, description="Optional comment")

class FeedbackRead(BaseModel):
    id: int
    rating: int
    challenge_id: int
    comment: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True