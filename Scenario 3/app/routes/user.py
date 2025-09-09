# User CRUD routes

from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.schemas.user import UserCreate, UserBase
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=dict)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email already exists
    existing_user = db.query(User).filter(User.username == user.username).first() | db.query(User).filter(User.email == user.email).first()
    if(existing_user):
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    # For new use
    # Hash the password before storing
    hashed_password = hash_password(user.password)

    # Creating a new user instance
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password
    )

    # Add to the session and commit to the database
    db.add(new_user) # Add the new user to the current database session
    db.commit() # Commit the transaction to save the new user
    db.refresh(new_user) # Refresh to get the new data from the database (like the generated ID)

    return {'id': new_user.id, 'username': new_user.username}