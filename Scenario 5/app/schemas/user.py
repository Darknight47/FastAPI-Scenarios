# User Schema
from pydantic import BaseModel, EmailStr, field_validator
import re

# Shared properties
class UserBase(BaseModel):
    username: str
    email: EmailStr


# Input
class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        return value


# Output
class UserRead(UserBase):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True