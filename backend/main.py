from fastapi import FastAPI
from app.infrastructure.api import users, assignments
from app.infrastructure.api.dependencies import db

app = FastAPI()
app.include_router(users.router, prefix="/api")
app.include_router(assignments.router, prefix="/api")

@app.get("/")
def test():
    return {"status": "ok"}

@app.get("/ping_db")
async def ping_db():
    await db.command("ping")
    return {"mongodb": "connected"}