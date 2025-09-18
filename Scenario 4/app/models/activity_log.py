# SQLALchemy model for ActivityLog
from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime, timezone
import enum

class ActivityType(str, enum.Enum):
    TASK_CREATED = "task_created"
    TASK_UPDATED = "task_updated"
    STATUS_CHANGED = "status_changed"
    TASK_ASSIGNED = "task_assigned"
    COMMENT_ADDED = "comment_added"
    OTHER = "other"

class ActivityLog(Base):
    __tablename__ = 'activity_logs'

    id = Column(Integer, primary_key=True, index=True)
    action_type = Column(Enum(ActivityType), default=ActivityType.OTHER, nullable=False)
    message = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # FK
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    # Optional
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)


    # Relationships
    user = relationship("User", back_populates="activity_logs")
    task = relationship("Task", back_populates="activity_logs")