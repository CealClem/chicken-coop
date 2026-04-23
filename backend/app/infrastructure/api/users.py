from app.application.use_cases.create_user_usecase import CreateUserUsecase
from app.application.use_cases.get_users_usecase import GetUsersUseCase
from app.domain.models.create_user_request import CreateUserRequest
from app.infrastructure.api.dependencies import get_db
from app.infrastructure.db.mongo_user_repository import MongoUserRepository
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase


router = APIRouter(prefix="/users")

def get_user_repository(db: AsyncIOMotorDatabase = Depends(get_db)):
    return MongoUserRepository(db)

def get_create_user_usecase(repo = Depends(get_user_repository)):
    return CreateUserUsecase(repo)

@router.post("/")
async def create_user_usecase(request: CreateUserRequest, use_case = Depends(get_create_user_usecase)):
    return await use_case.execute(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=request.password
    )

def get_get_users_usecase(repo = Depends(get_user_repository)):
    return GetUsersUseCase(repo)

@router.get("/")
async def get_users_usecase(use_case = Depends(get_get_users_usecase)):
    return await use_case.execute()