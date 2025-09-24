# TeamMembership Schema
from pydantic import BaseModel
from datetime import datetime
from app.models.team_membership import Role

# Input
class TeamMembershipCreate(BaseModel):
    user_id: int
    role: Role

# Output
class TeamMembershipRead(BaseModel):
    id: int
    user_id: int
    team_id: int
    joined_at: datetime

    class Config:
        from_attributes = True