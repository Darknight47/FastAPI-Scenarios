# Role Pydantic Schema
from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str | None = None

class RoleRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    # a special inner class where we can define configuration options for how your model behaves.
    # Hey Pydantic, here are some extra rules or behaviors for how to use this model.
    class Config:
        # Allows model to be created from ORM objects
        from_attributes = True