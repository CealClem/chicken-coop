from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.api import users, assignments
from app.infrastructure.api.dependencies import db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api")
app.include_router(assignments.router, prefix="/api")

@app.get("/ping_db")
async def ping_db():
    await db.command("ping")
    return {"mongodb": "connected"}
