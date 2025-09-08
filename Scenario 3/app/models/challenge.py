from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship
from app.models.challenge_tag import challenge_tags
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

    # Relationships
    
    # From a challenge, I want to access all feedbacks associated with it.
    # cascade="all, delete-orphan" ensures feedback is deleted if its parent user or challenge is removed.
    feedbacks = relationship('Feedback', back_populates='challenge', cascade='all, delete-orphan')
    
    # Many-to-many relationship with Path through the association table path_challenges.
    # back_populates creates a bidirectional link so we can do:
        # path.challenges → all challenges in a path
        # challenge.paths → all paths that include this challenge
    paths = relationship('Path', secondary='path_challenges', back_populates='challenges')
    
    # From a challenge, I want to access all progress entries associated with it.
    progress_entries = relationship('Progress', back_populates = 'challenge', cascade='all, delete-orphan')

    # Many-to-many relationship with Tag through the association table challenge_tags.
    # From a challenge, I want to access all tags associated with it.
    tags = relationship('Tag', secondary='challenge_tags', back_populates='challenges')