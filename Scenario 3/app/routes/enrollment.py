# CRUD operations for Enrollment
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.path import Path
from app.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead

# Create a router for enrollment-related endpoints
router = APIRouter(prefix="/enrollments", tags=['Enrollments'])

# ----------------- Enroll a user in a path -----------------
@router.post("/", response_model=EnrollmentRead)
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    # Check if the user exists
    user = db.query(User).filter(User.id == enrollment.user_id).first()
    if(not user):
        raise HTTPException(status_code=404, detail="User not found")

    # Checking if the path exists
    path = db.query(Path).filter(Path.id == enrollment.path_id).first()
    if(not path):
        raise HTTPException(status_code=404, detail="Path not found")

    # Checking if the user is already enrolled in the path
    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.user_id == enrollment.user_id,
        Enrollment.path_id == enrollment.path_id
    ).first()

    if(existing_enrollment):
        raise HTTPException(status_code=400, detail="User is already enrolled in this path")
    
    # Creating a new enrollment
    db_enrollment = Enrollment(
        user_id = enrollment.user_id,
        path_id = enrollment.path_id
    )

    # Add to the session and commit
    db.add(db_enrollment)
    # Commit the transaction
    db.commit()
    # Refresh the instance to get the generated ID and enrolled_at timestamp
    db.refresh(db_enrollment)
    return db_enrollment

# ----------------- Delete a user's enrollment in a path -----------------
# User sees a list of paths they’re enrolled in
# Each path has a button: Unenroll or Leave

@router.delete("/{enrollment_id}", response_model=dict)
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    # Check if the enrollment exists
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if(not enrollment):
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    db.delete(enrollment)
    db.commit()
    return{"detail": "Enrollment deleted successfully"}