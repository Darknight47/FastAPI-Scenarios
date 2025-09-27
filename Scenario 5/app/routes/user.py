# User CRUD Routes
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.utils.security import hash_password

# Creating an APIRouter
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    # Checking if the user already exists
    existing_user = db.query(User).filter(
        (User.username == user_in.username) | (User.email == user_in.email)
    ).first()
    
    if(existing_user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username or Email already exists.")
    
    # Hashing password
    hashed_pw = hash_password(user_in.password)

    # Creating a new user
    new_user = User(
        username = user_in.username,
        email = user_in.email,
        hashed_password = hashed_pw
    )

    # Saving new user to the DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # reload the user from the database, including any fields the DB auto-generated,

    # returning new user
    return new_user