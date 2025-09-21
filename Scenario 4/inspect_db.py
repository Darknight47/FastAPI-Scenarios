from app.db.database import engine
from sqlalchemy import inspect

def inspect_db():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("✅ Tables in the database:")
    for table in tables:
        print(f" - {table}")

if __name__ == "__main__":
    inspect_db()
