# CRUD APIs for Feedback
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.feedback import Feedback
from app.models.challenge import Challenge
from app.schemas.feedback import FeedbackCreate, FeedbackRead

router = APIRouter(prefix="/feedbacks", tags=['feedbacks'])

# ---------------------- Create feedback for a challenge ----------------------
# When a specific user submits feedback for a challenge
@router.post("/", response_model=FeedbackRead)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    # Check if the challenge exists
    challenge = db.query(Challenge).filter(Challenge.id == feedback.challenge_id).first()
    if(not challenge):
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    # Checking if feedback already exists for the challenge
    existing_feedback = db.query(Feedback).filter(Feedback.challenge_id == feedback.challenge_id).first()
    if(existing_feedback):
        raise HTTPException(status_code=400, detail="Feedback already submitted for this challenge.")
    
    new_feedback = Feedback(
        challenge_id=feedback.challenge_id,
        rating=feedback.rating,
        comment=feedback.comment
    )
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback