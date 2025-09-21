# TeamMembership SQLAlchemy model
# It connects User and Team and stores the user's role in the team (like "admin" or "member").

import datetime
from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy.types import Enum as SQLEnum  # Alias to avoid conflict
from enum import Enum

class Role(str, Enum):
    MEMBER = 'member'
    ADMIN = 'admin'

class TeamMembership(Base):
    __tablename__ = "team_memberships"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True) # Primary key column
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Foreign key to User table (child table side)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False) # Foreign key to Team table (child table side)
    role = Column(SQLEnum(Role), default=Role.MEMBER, nullable=False) # Role column with Enum type
    joined_at = Column(DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc)) # Timestamp column for when the user joined the team

    # Relationships

    user = relationship("User", back_populates="memberships")
    team = relationship("Team", back_populates="members")