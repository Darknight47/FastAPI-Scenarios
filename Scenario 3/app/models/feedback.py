from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # In relational databases, the child table holds the foreign key pointing to the parent table.
    # Feedback is the child table, User and Challenge are the parent tables.
    # A feedback belongs to one user and one challenge.

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'), nullabel=False)
    challenge_id = Column(Integer, ForeignKey('challenges.id'), nullable=False)

    # Relationships
    
    # This links the feedback to a user via the user_id foreign key.
    # From a feedback, I want to access the user who wrote it.
    author = relationship('User', back_populates='feedbacks')
    # This links the feedback to a challenge via the challenge_id foreign key.
    challenge = relationship('Challenge', back_populates='feedbacks')