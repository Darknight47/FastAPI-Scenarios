from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routes import tasks

async def lifespan(app: FastAPI):
    # Runs create_db_and_tables() once when the app starts.
    create_db_and_tables() # called once at startup.
    yield # Hands back the control to FastAPI to continue running the app.

# every time you run the app, it checks if the tables exist — and creates them if they don’t.

app = FastAPI(lifespan = lifespan)

# Registers all end-points defined in tasks.py
app.include_router(tasks.router)