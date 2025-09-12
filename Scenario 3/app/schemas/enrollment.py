# Schema for Enrollment
from pydantic import BaseModel
from datetime import datetime


# User registers → POST /users
# User browses paths → GET /paths
# User clicks “Enroll” on a path → triggers POST /enrollments

# At this point, your frontend knows:
# The path_id (from the clicked path)
# The user_id (from the logged-in user session)

class EnrollmentCreate(BaseModel):
    user_id: int
    path_id: int

class EnrollmentRead(BaseModel):
    id: int
    user_id: int
    path_id: int
    enrolled_at: datetime

    class Config:
        from_attributes = True