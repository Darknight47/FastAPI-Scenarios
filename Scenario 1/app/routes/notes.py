from fastapi import APIRouter
from sqlmodel import Session, select
from app.models import Note, NoteCreate
from app.database import engine


# Creates a modular router for note-related endpoints.
router = APIRouter()


# The engine is a long-lived object that knows how to connect to your database.
# It holds the connection string (sqlite:///./notes.db) and manages the low-level communication.
# Think of engine as the elevator system in a building — it’s always there, ready to move people (queries) up and down between your app and the database.

# A Session is a short-lived object that wraps a single interaction with the database.
# It’s used to read/write data, and it tracks changes until you commit them.

# We create a new session every time you want to talk to the database.
# It lasts only as long as the with Session(engine) as session: block.

# Why We Use It Like That:
##Keeps things clean and thread-safe.
## Avoids memory leaks or dangling connections.
## Makes sure each transaction is isolated.

@router.post("/notes")
def create_note(note_create: NoteCreate):
    note = Note(**note_create.model_dump())
    # Opens a connection to the database.
    with Session(engine) as session: 
        session.add(note) # Adds the new note to the database (but not yet saved).
        session.commit() # Saves the changes.
        session.refresh(note) # Reloads the note from the database (to get the auto-generated id and created_at).
        return note

@router.get("/notes")
def get_notes():
    with Session(engine) as session:
        statement = select(Note) # Builds a SQL query to fetch all rows from the note table.
        results = session.exec(statement) # Executes the query.
        return results.all() # Returns all notes as a list of Note objects, which FastAPI automatically converts to JSON.