from sqlmodel import SQLModel, create_engine

# Points to a local SQLite file named tasks.db
DATABASE_URL = "sqlite:///./tasks.db"

# Connects your app to the database
engine = create_engine(DATABASE_URL, echo = True)

# Creates tables based on your SQLModel classes
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)