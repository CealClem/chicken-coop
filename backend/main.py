from fastapi import FastAPI
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

mongodb_url = os.getenv("MONGODB_URL")

client = AsyncIOMotorClient(mongodb_url)
db = client.chickencoop

app = FastAPI()
@app.get("/")
def test():
    return {"status": "ok"}

@app.get("/ping_db")
async def ping_db():
    await db.command("ping")
    return {"mongodb": "connected"}