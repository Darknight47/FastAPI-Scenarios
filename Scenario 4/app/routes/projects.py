# Projects and Task CRUD operations
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.task import Task, TaskPriority, TaskStatus
from app.schemas.task import TaskCreate, TaskRead
from app.models.project import Project
from app.models.user import User
from typing import List, Optional

router = APIRouter(prefix="/projects", tags=["Projects"])

# --------------------- Creating a task for the project --------------
@router.post("/{project_id}/tasks/", response_model=TaskRead)
def create_task_for_project(project_id: int, task_in: TaskCreate, db: Session = Depends(get_db)):
    # Checking if the project exists
    project = db.query(Project).filter(Project.id == project_id).first()
    if(not project):
        raise HTTPException(status_code=404, detail="Project not found.")
    
    # checking if assignee is provided, validating user exists. (This is optional)
    if(task_in.assigne_id):
        user = db.query(User).filter(User.id == task_in.assigne_id).first()
        if (not user):
            raise HTTPException(status_code=404, detail="Assignee user not found.")

    # Creating a new task
    new_task = Task(
        title = task_in.title,
        description = task_in.description,
        status = task_in.status,
        priority = task_in.priority,
        due_date = task_in.due_date,
        assignee_id = task_in.assigne_id,
        project_id = project_id
    )

    # Saving
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# ------------------------ Getting (Filtering) tasks by status, priority, due_date ----------------------
@router.get("/{project_id}/tasks/", response_model=List[TaskRead])
def list_tasks_for_project(project_id: int, 
                           status: Optional[TaskStatus] = None, 
                           priority: Optional[TaskPriority] = None,
                           due_date_before: Optional[datetime] = None,
                           db: Session = Depends(get_db)):
    # Checking if the project exists
    project = db.query(Project).filter(Project.id == project_id).first()
    if(not project):
        raise HTTPException(status_code=404, detail="Project not found.")
    
    query = db.query(Task).filter(Task.project_id == project_id)

    if(status):
        query = query.filter(Task).filter(Task.status == status) # Adds a 'WHERE' condition
    
    if(priority):
        query = query.filter(Task).filter(Task.priority == priority) # Adds another condition
    
    if(due_date_before):
        query = query.filter(Task).filter(Task.due_date == due_date_before) # Adds another condition
    
    return query.all()