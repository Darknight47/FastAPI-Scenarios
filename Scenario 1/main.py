from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routes import notes

# lifespan() is an async context manager that runs setup logic before the app starts.
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables() # create_db_and_tables() is called once at startup.
    yield # yield hands control back to FastAPI to continue running the app.

# every time you run the app, it checks if the tables exist — and creates them if they don’t.

app = FastAPI(lifespan=lifespan)

app.include_router(notes.router) # Registers all endpoints defined in notes.py with the main app.