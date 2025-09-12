# CRUD Operations for Path
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.path import Path
from app.models.challenge import Challenge
from app.schemas.path import PathCreate, PathRead


# Create a router for path-related endpoints
router = APIRouter(prefix="/paths", tags=['Paths']) 

# ----------------- Create a new path -----------------
@router.post("/", response_model=PathRead)
def create_path(path: PathCreate, db: Session = Depends(get_db)):
    # Checking if a path with the same title already exists
    existing_path = db.query(Path).filter(Path.title == path.title).first()
    if(existing_path):
        raise HTTPException(status_code=400, detail="Path with this title already exists")
    
    new_path = Path(title=path.title, description=path.description)

    # Add to the session and commit
    db.add(new_path)
    # Commit the transaction
    db.commit()
    # Refresh the instance to get the generated ID
    db.refresh(new_path)
    
    return new_path

# ----------------- Get all paths -----------------
@router.get("/", response_model=list[PathRead])
def get_paths(db: Session = Depends(get_db)):
    paths = db.query(Path).all()
    return paths

# ----------------- Get the number of enrollments for a path -----------------
@router.get("/{path_id}/enrollments/count", response_model=int)
def get_enrollment_count(path_id: int, db: Session = Depends(get_db)):
    path = db.query(Path).filter(Path.id == path_id).first()
    if(not path):
        raise HTTPException(status_code=404, detail="Path not found.")
    
    enrollment_count = db.query(Path).filter(Path.id == path_id).count()
    
    return enrollment_count


# ----------------- Attach a challenge to a path --------------------
@router.post("/{path_id}/challenges/{challenge_id}", response_model=dict)
def attach_challenge_to_path(path_id: int, challenge_id: int, db: Session = Depends(get_db)):
    path = db.query(Path).filter(Path.id == path_id).first()
    if(not path):
        raise HTTPException(status_code=404, detail="Path not found.")
    
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if(not challenge):
        raise HTTPException(status_code=404, detail="Challenge not found.")
    
    if(challenge in path.challenges):
        raise HTTPException(status_code=400, detail="Challenge already attached to the path.")
    
    # Even though challenges is a relationship, SQLAlchemy treats it as a dynamic collection when it's a one-to-many or many-to-many relationship. 
    # Under the hood, it's not a plain list — it's a special InstrumentedList, which:
    # Tracks changes (additions/removals)
    # Automatically updates the association table (path_challenges)
    # Integrates with the session and flush logic
    path.challenges.append(challenge)

    db.commit()
    db.refresh(path)
    return {"message": "Challenge attached to path successfully."}

# ----------------- Detach a challenge from a path --------------------
@router.delete("/{path_id}/challenges/{challenge_id}", response_model=dict)
def detach_challenge_from_path(path_id: int, challenge_id: int, db: Session = Depends(get_db)):
    path = db.query(Path).filter(Path.id == path_id).first()
    if(not path):
        raise HTTPException(status_code=404, detail="Path not found.")
    
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if(not challenge):
        raise HTTPException(status_code=404, detail="Challenge not found.")
    
    if(challenge not in path.challenges):
        raise HTTPException(status_code=400, detail="Challenge is not attached to the path.")
    
    path.challenges.remove(challenge)

    db.commit()
    db.refresh(path)
    return {"message": "Challenge detached from path successfully."}
