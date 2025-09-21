# Team CRUD Operations
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamRead

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