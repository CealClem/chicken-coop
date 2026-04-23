from motor.motor_asyncio import AsyncIOMotorDatabase
from app.domain.models.user import User
from app.domain.ports.user_repository import AbstractUserRepository


class MongoUserRepository(AbstractUserRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.users

    async def create_user(self, user: User) -> User:
        result = await self.collection.insert_one(user.model_dump(exclude={"id"}))
        user.id = str(result.inserted_id)
        return user
    
    async def get_users(self) -> list[User]:
        users = await self.collection.find().to_list(length=None)
        for user in users:            
            user["_id"] = str(user["_id"])
        return [User(**user) for user in users]

    async def get_user_by_id(self, user_id: str) -> User | None:
        user = await self.collection.find_one({"_id": user_id})
        if user:
            user["_id"] = str(user["_id"])
            return User(**user)
        return None
    
    async def get_user_by_email(self, email: str) -> User | None:
        user = await self.collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])
            return User(**user)
        return None
    
    async def update_user(self, user_id: str, updated_fields: User) -> User:
        result = await self.collection.update_one(
            {"_id": user_id},
            {"$set": updated_fields.model_dump()}
        )
        assert result.modified_count > 0
        return await self.get_user_by_id(user_id)
    
    async def delete_user(self, user_id: str) -> None:
        result = await self.collection.delete_one({"_id": user_id})
        assert result.deleted_count == 1