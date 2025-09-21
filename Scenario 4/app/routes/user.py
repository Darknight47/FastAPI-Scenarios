# User CRUD Routes

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.utils.security import hash_password

# creates an APIRouter, which is like a mini FastAPI app focused on a specific section of your API — here, for /users.
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Checking if user already exists
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if(existing_user):
        raise HTTPException(status_code=400, detail="Username or Email Already Registered!")
    
    # Creating a new user
    # Hasing Password
    hashed_pass = hash_password(user.password)

    # a new user
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pass
    )

    # Adding the new user to the DB
    db.add(new_user)
    db.commit() # Committing the transaction to save the user
    db.refresh(new_user) # for getting the new data from DB.

    return new_user