# Database file
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" #SQLite URL for a file-based DB

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
# It opens the session before your logic runs, and closes it cleanly when done — which is important for avoiding DB leaks.
def get_db():
    db: Session = SessionLocal()
    try: 
        yield db
    finally:
        db.close()