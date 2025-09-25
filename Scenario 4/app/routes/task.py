# Task and Comment CRUD Operations

from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.comment import Comment
from app.models.task import Task
from app.schemas.comment import CommentCreate, CommentRead
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# ------------------------- Creating a comment -------------------------
@router.post("/{task_id}/comments/", response_model=CommentRead)
def create_comment_on_task(
    task_id: int,
    comment_in: CommentCreate,
    db: Session = Depends(get_db)
):
    # 1. Ensure the task exists
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")

    # 2. Ensure the author (user) exists
    user = db.query(User).filter(User.id == comment_in.author_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User (author) not found.")

    # 3. Create the comment
    comment = Comment(
        content=comment_in.content,
        author_id=comment_in.author_id,
        task_id=task_id
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment