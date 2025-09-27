from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import Base, engine
from app.routes import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating DB Tables ...")
    Base.metadata.create_all(bind=engine)
    print("Done!")
    yield  # app runs after this

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)