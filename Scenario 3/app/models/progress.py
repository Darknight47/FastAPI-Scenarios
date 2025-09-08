from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key = True)
    completed = Column(Boolean, default = False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    challenge_id = Column(Integer, ForeignKey('challenges.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='progress_entries')
    challenge = relationship('Challenge', back_populates='progress_entries')