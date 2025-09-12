from fastapi import FastAPI
from app.routes import user, role, path, enrollment

app = FastAPI()

# Including router from user.py
app.include_router(user.router)
# Including router from role.py
app.include_router(role.router)
# Including router from path.py
app.include_router(path.router)
# Including router from enrollment.py
app.include_router(enrollment.router)