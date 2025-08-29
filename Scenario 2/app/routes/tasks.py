from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select
from typing import Optional
from app.models import Task, TaskCreate, TaskUpdate, TaskStatus
from app.database import engine

# Session is a class from SQLAlchemy (which SQLModel builds on top of). It’s your gateway to:
# Executing queries
# Adding, updating, deleting records
# Managing transactions
# Caching and tracking changes


# Creating a modular router for task-related endpoints.
router = APIRouter()

# We create a new session every time we want to taslk to the DB
# It lasts only as long as the 'with Session(engine) as session:' block of code.
# Uses for: avoiding memory leaks or dangling connections, isolating each transaction, thread-safe.

# --------------------------- Creating a new task
@router.post("/tasks")
def create_task(task_data: TaskCreate):
    task = Task(**task_data.dict())
    # Opening a connection to the database.
    with Session(engine) as session:
        # Adding the new task to the DB (not saved for now)
        session.add(task)
        # Saving the changes
        session.commit()
        # Reloading the task from the DB for the getting the auto-generated ID and created_at
        session.refresh(task)
        # Returning the new task
        return task

# --------------------------- Retrieving all the tasks from the DB
#@router.get("/tasks")
#def get_tasks():
    # Opening a connection to the db.
#    print("allll----------")
#    with Session(engine) as session:
#        statement = select(Task) # a SQL query to fetch all the rows from the 'Task' table.
#        results = session.exec(statement) # Executing the query
#        return results.all()

# --------------------------- Filtering tasks based on their status from the DB OR Retrieving all the tasks from the DB
# Accepts an optional query parameter like ?status=pending
@router.get("/tasks")
def get_tasks(status: Optional[TaskStatus] = Query(None)):
    with Session(engine) as session:
        statement = select(Task)
        if(status):
            # If provided, adds a WHERE clause to the SQL query
            statement = statement.where(Task.status == status)
            print("Status filter received:", status)
            print("Status filter received:", status)
        # Only matching tasks are returned, directly from the database
        results = session.exec(statement)
        return results.all()


# --------------------------- Retrieving a specific task from the DB
@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Opening a connection to the db.
    with Session(engine) as session:
        # Fetches the task by 'primary key'.
        task = session.get(Task, task_id)
        if(not task):
            raise HTTPException(status_code=404, detail="Task not found.")
        return task


# --------------------------- Updating a specific task from the DB
@router.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    # Opening a connection to the db.
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if(not task):
            raise HTTPException(status_code = 404, detail="Task not found.")

        # Applies only the fields that were sent (exclude_unset=True)
        # Only include fields that were actually provided by the client 
        # Skip fields that were left out or have default values
        task_data = task_update.dict(exclude_unset = True)

        for key, value in task_data.items():
            setattr(task, key, value)
        
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


# --------------------------- Deleting a specific task from the DB
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Opening a connection with the DB
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if(not task):
            raise HTTPException(status_code= 404, detail="Task not found.")

        session.delete(task)
        session.commit()

        return {"Message": f"Task {task_id} has been deleted!"}