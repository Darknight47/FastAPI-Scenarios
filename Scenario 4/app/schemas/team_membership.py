# TeamMembership Schema
from pydantic import BaseModel
from datetime import datetime
from app.models.team_membership import Role

# Input
class TeamMembershipCreate(BaseModel):
    user_id: int
    role: Role.MEMBER

# Output
class TeamMembershipRead(BaseModel):
    id: int
    team_id: int
    joined_at: datetime

    class Cofig:
        from_attributes = True