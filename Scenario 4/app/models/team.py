# Team SQLALchemy model
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.team_membership import TeamMembership

class Team(Base):
    __tablename__ = "teams" # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Id Column (primary key)
    name = Column(String, unique=True, index=True, nullable=False)  # Name Column
    description = Column(String, nullable=True)  # Description Column (optional)

    # Relationships
    members = relationship("TeamMembership", back_populates="team", cascade="all, delete-orphan")
    # 'members' is a list of TeamMembership instances associated with this team.

    projects = relationship("Project", back_populates='team', cascade='all, delete-orphan')
