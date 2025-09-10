# User CRUD routes

from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.models.role import Role
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.security import hash_password

# creates an APIRouter, which is like a mini FastAPI app focused on a specific section of your API — here, for /users.
# The prefix means all routes here will start with /users, and the tags help group them in the docs.
router = APIRouter(prefix="/users", tags=["Users"])

# The endpoint becomes POST /users/ in the final app.
# It expects a UserCreate object in the request body and uses the get_db dependency (Dependency Injection) to get a database session.
@router.post("/", response_model=dict)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email already exists
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)).first()
    if(existing_user):
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    # For new use
    # Hash the password before storing
    hashed_password = hash_password(user.password)

    # Fetch default role ('user' is the default role name, adjust as necessary)
    default_role = db.query(Role).filter(Role.name == 'user').first()
    if(not default_role):
        raise HTTPException(status_code=500, detail="Default role not found")
        

    # Creating a new user instance (default role is 'user')
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password,
        role_id = default_role.id
    )

    # Add to the session and commit to the database
    db.add(new_user) # Add the new user to the current database session
    db.commit() # Commit the transaction to save the new user
    db.refresh(new_user) # Refresh to get the new data from the database (like the generated ID)

    return {'id': new_user.id, 'username': new_user.username}

# --------------------- GET ALL ----------------------
# The endpoint becomes GET /users/ in the final app.
# It retrieves all users from the database and returns them as a list of UserRead objects. (Not recommended for production due to potential data volume)
# We should retrieve data with guardrailes like pagination, filtering, etc.
@router.get("/", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# ---------------------- Get by ID -------------------
# The endpoint becomes GET /users/{user_id} in the final app.
# It retrieves a user by their ID and returns it as a UserRead object.
@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if(not user):
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ---------------------- Delete by ID -------------------
# The endpoint becomes DELETE /users/{user_id} in the final app.
# It deletes a user by their ID and returns a success message.
@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if(not user):
        raise HTTPException(status_code=404, detail="User not found! cannot delete.")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully!"}