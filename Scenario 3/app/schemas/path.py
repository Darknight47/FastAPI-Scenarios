# Pydantic Schema for Path
from pydantic import BaseModel

class PathCreate(BaseModel):
    title: str
    description: str | None = None

class PathRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    class Config:
        from_attributes = True