from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.chickencoop

def get_db():
    return db