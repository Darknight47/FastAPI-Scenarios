# CRUD operations for Tag
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagRead


router = APIRouter(prefix="/tags", tags=['Tags'])


# ---------------- Creating a new Tag ----------------
@router.post("/", response_model=TagRead)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    existing_tag = db.query(Tag).filter(Tag.name == tag.name).first()

    if(existing_tag):
        raise HTTPException(status_code=400, detail="Tag already exists")
    
    new_tag = Tag(name=tag.name)

    # Add to the session and commit
    db.add(new_tag)
    # Commit the transaction
    db.commit()
    # Refresh the instance to get the generated ID
    db.refresh(new_tag)

    return new_tag