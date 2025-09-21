# Team Schema!

from typing import Optional
from pydantic import BaseModel

class TeamBase(BaseModel):
    name: str
    description: Optional[str] = None

# Input
class TeamCreate(TeamBase):
    pass


# Output
class TeamRead(TeamBase):
    id: int
    
    class Config:
        from_attributes = True