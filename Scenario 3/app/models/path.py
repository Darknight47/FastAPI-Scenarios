from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship
from enum import Enum
from app.database import Base


class Path(Base):
    __tablename__ = 'paths'

    id = Column(Integer, primary_key= True)
    title = Column(String, nullable= False)
    description = Column(Text, nullable=True)

    # Relationships
    # From a path, I want to access all enrollments associated with it.
    enrollments = relationship('Enrollment', back_populates='path', cascade='all, delete-orphan')