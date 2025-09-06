from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String)
    hashed_password = Column(String) # is stored securely — never expose it via Pydantic schemas.

    # A user belongs to one role → so we store role_id in the User table.
    # In relational databases, the child table holds the foreign key pointing to the parent table.
    # User is the child table, Role is the parent table.

    # One-To-Many relationship: A role can have many users, but a user has only one role.

    role_id = Column(Integer, ForeignKey('roles.id')) # is the foreign key pointing to Role. 
    role = relationship('Role', back_populates='users') # the back-reference to the role of this user.

    feedbacks = relationship('Feedback', back_populates='author', cascade='all, delete-orphan')