# Team & TeamMembership CRUD Operations
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.team import Team
from app.models.user import User
from app.models.team_membership import TeamMembership
from app.schemas.team import TeamCreate, TeamRead
from app.schemas.team_membership import TeamMembershipCreate, TeamMembershipRead

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    # Checking if the team already exists
    existing_team = db.query(Team).filter(Team.name == team.name).first()
    if(existing_team):
        raise HTTPException(status_code=400, detail="Team already exists.")
    
    # Creating a team
    new_team = Team(
        name = team.name,
        description = team.description
    )

    # Adding to the DB
    db.add(new_team)
    db.commit()
    db.refresh()

    return new_team

# -------------------- Get a team with ID ----------------------
@router.get("/{team_id}", response_model=TeamRead)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if(not team):
        raise HTTPException(status_code=400, detail="Team not found.")
    return team

# ------------------ Registering a team member ----------------------
@router.post("{team_id}/members/", response_model=TeamMembershipRead)
def add_member_to_team(team_id: int, membership: TeamMembershipCreate, db: Session = Depends(get_db)):
    # Checking if a team exists
    team = db.query(Team).filter(Team.id == team_id).first()
    if(not team):
        raise HTTPException(status_code=404, detail="Not team found.")
    
    # Checking if the user exists.
    user = db.query(User).filter(User.id == membership.user_id).first()
    if(not user):
        raise HTTPException(status_code=404, detail="Not user found.")
    
    # Checking if the user already been registered (preventing double membership).
    existing_membership = db.query(TeamMembership).filter(
        TeamMembership.user_id == membership.user_id,
        TeamMembership.team_id == team_id
    ).first()

    if(existing_membership):
        raise HTTPException(status_code=400, detail="The user is already a member of this team.")
    
    # Creating the membership
    new_membership = TeamMembership(
        user_id = membership.user_id,
        team_id = team_id,
        role = membership.role
    )

    # Storing the membership 
    db.add(new_membership)
    db.commit()
    db.refresh(new_membership)

    return new_membership
