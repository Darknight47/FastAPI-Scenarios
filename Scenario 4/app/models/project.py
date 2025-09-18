# SQLAlchemy Project Model
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    # FK
    # required (each project must belong to a team)
    team_id = Column(Integer, ForeignKey('teams.id', ondelete='CASCADE'), nullable=False)
    # ondelete="CASCADE": deleting a team deletes its projects

    # Relationships
    
    team = relationship('Team', back_populates='projects')

    tasks = relationship("Task", back_populates='project', cascade='all, delete-orphan')