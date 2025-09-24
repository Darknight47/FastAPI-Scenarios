# Team & TeamMembership CRUD Operations
from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamRead
from app.models.user import User
from app.models.team_membership import TeamMembership
from app.schemas.team_membership import TeamMembershipCreate, TeamMembershipRead
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead
from typing import List
from fastapi import status


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
    db.refresh(new_team)

    return new_team


# ------------------ Registering a team member ----------------------
@router.post("/{team_id}/members/", response_model=TeamMembershipRead)
def add_member_to_team(team_id: int, membership: TeamMembershipCreate = Body(...), db: Session = Depends(get_db)):
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

# ---------------------- Removing a membership ------------------------
@router.delete("/{team_id}/members/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_member_from_team(team_id: int, user_id: int, db: Session = Depends(get_db)):
    # Checking if membership exists
    membership = db.query(TeamMembership).filter(
        TeamMembership.user_id == user_id,
        TeamMembership.team_id == team_id
    ).first()

    if(not membership):
        raise HTTPException(status_code=404, detail="Membership not found.")
    
    db.delete(membership)
    db.commit()
    return

# ------------------------- Getting members of a team ----------------------
@router.get("/{team_id}/members/", response_model=List[TeamMembershipRead])
def get_team_members(team_id: int, db: Session = Depends(get_db)):
    # checking if the team exists.
    team = db.query(Team).filter(Team.id == team_id)
    if(not team):
        raise HTTPException(status_code=404, detail="Team not found.")
    
    members = db.query(TeamMembership).filter(
        TeamMembership.team_id == team_id
    ).all()

    return members


# ------------------------- Creating a project for the team ---------------------
# Projects belong to teams
@router.post("/{team_id}/projects/", response_model=ProjectRead)
def create_project_for_team(team_id: int, project_in: ProjectCreate, db: Session = Depends(get_db)):
    # Checking if the team exists
    team = db.query(Team).filter(Team.id == team_id).first()
    if(not team):
        raise HTTPException(status_code=404, detail="Team not found.")
    
    # Creating a project
    new_project = Project(
        name = project_in.name,
        description = project_in.description,
        due_date = project_in.due_date,
        team_id = team_id
    )

    # Saving
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project