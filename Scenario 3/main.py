from fastapi import FastAPI
from app.routes import user

app = FastAPI()

# Including router from user.py
app.include_router(user.router)