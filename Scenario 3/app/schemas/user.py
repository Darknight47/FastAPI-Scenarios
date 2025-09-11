# Pydantic User Schema
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

# Class for creating a new user, extends UserBase and adds a password field
class UserCreate(UserBase):
    password: str # Plain password, it will be hashed before storing

# Class for reading user data, extends UserBase and adds an id field
class UserRead(UserBase):
    id: int

    # a special inner class where we can define configuration options for how your model behaves.
    # Hey Pydantic, here are some extra rules or behaviors for how to use this model.
    class Config:
        # Allows model to be created from ORM objects
        from_attributes = True

# Class for updating user data, all fields are optional
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None