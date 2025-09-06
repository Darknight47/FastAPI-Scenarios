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

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'), nullabel=False)
    challenge_id = Column(Integer, ForeignKey('challenges.id'), nullable=False)

    # Relationships
    author = relationship('User', back_populates='feedbacks')
    challenge = relationship('Challenge', back_populates='feedbacks')