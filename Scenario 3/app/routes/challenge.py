# CRUD operations for Challenge
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.challenge import Challenge, DifficultyLevel
from app.models.tag import Tag
from app.schemas.challenge import ChallengeCreate, ChallengeRead

router = APIRouter(prefix="/challenges", tags=['challenges'])

# ---------------------- Create a new challenge ----------------------
@router.post("/", response_model=ChallengeRead)
def create_challenge(challenge: ChallengeCreate, db: Session = Depends(get_db)):
    db_challenge= Challenge(
        title=challenge.title,
        description=challenge.description,
        difficulty=challenge.difficulty
    )
    # Fetch and associate tags
    if(challenge.tag_ids):
        tags = db.query(Tag).filter(Tag.id.in_(challenge.tag_ids)).all()
        challenge.tags = tags
    
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge

# ---------------------- Delete a challenge by ID ----------------------
@router.post("/{challenge_id}", response_model=dict)
def delete_challenge(challenge_id: int, db: Session = Depends(get_db)):
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if(not challenge):
        raise HTTPException(status_code=404, detail="Challenge not found.")
    db.delete(challenge)
    db.commit()
    return {"detail": "Challenge deleted successfully."}
