from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
# we’re using SQLModel, which is a hybrid of:

# Pydantic’s BaseModel → for data validation and serialization
# SQLAlchemy’s declarative base → for database table mapping


# Data Model
# The class name Note becomes the table name in SQLite (by default, lowercase: note)
# Example note-table:
# id	title	content	created_at
# 1	"Groceries"	"Buy milk and eggs"	2025-08-26T19:30:00

class NoteBase(SQLModel):
    title: str
    content: str

class Note(NoteBase, table=True):
    id: int | None = Field(default=None, primary_key=True) # id: Auto-incrementing primary key.
    # instead of setting a fixed default like default=datetime.utcnow() (which would freeze the time at app startup), 
    # default_factory ensures the time is fresh every time a new note is created.
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    # When a new Note is created and no created_at is provided, FastAPI will call datetime.utcnow() at that moment to generate a default value.

# For shared files.
class NoteCreate(NoteBase):
    pass
