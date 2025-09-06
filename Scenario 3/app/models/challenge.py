from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship
from enum import Enum
from app.database import Base

class DifficultyLevel(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class Challenge(Base):
    __tablename__ = 'challenges'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    difficulty = Column(SqlEnum(DifficultyLevel))

    # cascade="all, delete-orphan" ensures feedback is deleted if its parent user or challenge is removed.
    feedbacks = relationship('Feedback', back_populates='challenge', cascade='all, delete-orphan')