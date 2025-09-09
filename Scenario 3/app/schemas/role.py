# Role Pydantic Schema
from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str | None = None

class RoleRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True