# CRUD Operations for Path
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.path import Path
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
            