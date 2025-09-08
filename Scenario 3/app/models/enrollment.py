from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from enum import Enum
from app.database import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key = True)
    enrolled_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    path_id = Column(Integer, ForeignKey('paths.id'), nullable=False)

    # Relationships
    
    # 'User' refers to the User model (class), it must match the exact class name.
    # This enrollment belongs to a user. On the User side, the relationship is called enrollments
    user = relationship('User', back_populates='enrollments')
    path = relationship('Path', back_populates='enrollments')
