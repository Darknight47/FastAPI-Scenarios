# User SQLAlchemy Model / Table
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users" # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True) # Primary key column 
    # Indexes improve query performance, especially for filtering and searching operations.
    username = Column(String, unique=True, index=True, nullable=False) # Username column
    email = Column(String, unique=True, index=True, nullable=False) # Email column
    hashed_password = Column(String, nullable=False) 

    # Relationships 