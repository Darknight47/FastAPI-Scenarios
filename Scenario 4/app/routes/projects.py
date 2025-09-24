# Projects and Task CRUD operations
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead
from app.models.project import Project
from app.models.user import User


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