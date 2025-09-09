from fastapi import FastAPI
from app.routes import user
from app.routes import role

app = FastAPI()

# Including router from user.py
app.include_router(user.router)
# Including router from role.py
app.include_router(role.router)