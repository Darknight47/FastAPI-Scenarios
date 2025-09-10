from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Connection String for the SQLite database
DATABASE_URL = "postgresql://admin:admin@localhost:5431/scen3"

# The engine, which is the core interface between SQLAlchemy and your actual database.
# engine = create_engine(
#     DATABASE_URL, connect_args = {"check_same_thread": False}
#     # SQLite, by default, doesn’t allow the same connection to be used in multiple threads.
#     # The connect_args parameter with check_same_thread set to False allows the connection to be shared across threads.
# )

engine = create_engine(DATABASE_URL, echo=True)

# autocommit=False: You manually control when changes are committed.
# autoflush=False: Changes aren’t sent to the database until we flush or commit. This gives us more control (and avoids surprises).
# A factory - creates new DB Session objects when called.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy uses this Base class to track 
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