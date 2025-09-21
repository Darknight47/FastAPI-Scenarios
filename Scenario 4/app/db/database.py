# Database file for: 
# SQLAlchemy engine
# SessionLocal
# Base class
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # SQLite URL for a file-based database named test.db in the current directory. (just in case, later we'll change it to PostgreSQL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False} # only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependency that provides a database session to path operations."""
    db: Session = SessionLocal() # creates a new session — think of it like opening a temporary connection to the database.
    try:
        yield db # Instead of returning db, it yields it. This allows FastAPI to: 
        # Inject the session into your path operation (endpoint),
        # Use it during the request,
        # Then automatically go to the finally block when done.
    finally:
        db.close() 
        # Once the request is finished (even if there was an error), the session is closed.