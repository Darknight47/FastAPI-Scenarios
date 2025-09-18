# SQLALchemy model for Comment
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime, timezone

class Comment(Base):
    __tablename__= "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # FK
    author_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    author = relationship("User", back_populates="comments")
    task = relationship("Task", back_populates="comments")