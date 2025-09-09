# CRUD Operations for Role
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleRead

router = APIRouter(prefix="/roles", tags=['Roles'])

@router.post("/", response_model=RoleRead)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    existing_role = db.query(Role).filter(Role.name == role.name).first()
    if(existing_role):
        raise HTTPException(status_code=400, detail="Role already exists")
    
    new_role = Role(name=role.name, description=role.description)

    # Add to the session and commit
    db.add(new_role)
    # Commit the transaction
    db.commit()
    # Refresh the instance to get the generated ID
    db.refresh(new_role)
    
    return new_role

@router.get("/", response_model=list[RoleRead])
def get_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).all()
    return roles