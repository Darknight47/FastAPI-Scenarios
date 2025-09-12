# Challenge schemas
from pydantic import BaseModel
from typing import List, Optional
from app.models.challenge import DifficultyLevel
from app.schemas.tag import TagRead

# A pydantic schema for creating a challenge
class ChallengeCreate(BaseModel):
    title: str
    description: Optional[str] = None
    difficulty: DifficultyLevel
    # Getting tag IDs to associate with the challenge
    tag_ids: Optional[List[int]] = []


class ChallengeRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    difficulty: DifficultyLevel
    tags: List[TagRead] = []