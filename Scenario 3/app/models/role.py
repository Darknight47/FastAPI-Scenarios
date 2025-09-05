from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    # A role can have many users → so we define users = relationship("User") in the Role model.
    # One-To-Many relationship: A role can have many users, but a user has only one role.

    users = relationship('User', back_populates = 'role') # the back-reference to all users with that role.
