# User SQLAlchemy Model / Table
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users" # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True) # Primary key column 
    # Indexes improve query performance, especially for filtering and searching operations.
    username = Column(String, unique=True, index=True, nullable=False) # Username column
    email = Column(String, unique=True, index=True, nullable=False) # Email column
    hashed_password = Column(String, nullable=False) 

    # Relationships 

    # 'memberships' is a list of TeamMembership instances associated with this user.
    # If user is deleted, all their team memberships are also deleted.
    memberships = relationship("TeamMembership", back_populates="user", cascade="all, delete-orphan")
    # If user is deleted, all their comments are also deleted.
    comments = relationship("Comment", back_populates='author', cascade="all, delete-orphan")