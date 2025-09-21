from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import Base  #
from app.db.database import engine  # your SQLAlchemy engine
from app.models.user import User
from app.models.team import Team
from app.models.team_membership import TeamMembership
from app.models.project import Project
from app.models.task import Task
from app.models.comment import Comment
from app.models.activity_log import ActivityLog

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating DB Tables ...")
    Base.metadata.create_all(bind=engine)
    print("Done!")
    yield  # app runs after this
    # Optional: add shutdown logic here

app = FastAPI(lifespan=lifespan)
