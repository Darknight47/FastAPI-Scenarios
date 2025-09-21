# User Schema
from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Input: User creation
class UserCreate(UserBase):
    password: str

# Output: Public user info
class UserRead(UserBase):
    id: int
    username: str

    class Config:
        from_attributes = True