from sqlmodel import SQLModel, create_engine

# sqlite:// → Specifies the database type (SQLite).
# ./notes.db → Tells it to store the database file in the current directory.
DATABASE_URL = "sqlite:///./notes.db"

# Manages the connection pool.
# Sends SQL queries to the database.
# Receives results back.
engine = create_engine(DATABASE_URL, echo=True)
# Think of it as the bridge between your Python code and the actual database.

# The engine is a long-lived object that knows how to connect to your database.
# It holds the connection string (sqlite:///./notes.db) and manages the low-level communication.
# Think of engine as the elevator system in a building — it’s always there, ready to move people (queries) up and down between your app and the database.


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)