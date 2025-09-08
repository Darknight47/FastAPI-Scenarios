from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True, nullable=False)

    # Relationships
    # From a tag, I want to access all challenges associated with it.
    # Many-to-many relationship with Challenge through the association table challenge_tags.
    challenges = relationship('Challenge', secondary='challenge_tags', back_populates='tags')