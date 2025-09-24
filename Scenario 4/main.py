from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import Base  #
from app.db.database import engine  # your SQLAlchemy engine
from app.routes import user, team, projects

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating DB Tables ...")
    Base.metadata.create_all(bind=engine)
    print("Done!")
    yield  # app runs after this
    # Optional: add shutdown logic here

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(team.router)
app.include_router(projects.router)