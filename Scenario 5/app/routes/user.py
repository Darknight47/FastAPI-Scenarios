# User CRUD Routes
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import LogInInput, UserCreate, UserRead
from app.utils.security import hash_password, verify_password

# Creating an APIRouter
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=UserRead)
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


# Login
@router.post("/login")
def login(login_data: LogInInput, db: Session = Depends(get_db)):
    # Checking if the user exists
    existing_user = db.query(User).filter(
        (User.username == login_data.username_or_email) | 
        (User.email == login_data.username_or_email)
    ).first()

    if(not existing_user):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Username/email or password.")
    
    if(not verify_password(login_data.password, existing_user.hashed_password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username/email or password"
        )
    
    # Creating JWT Token
    access_token = create_access_token()
    
    
    