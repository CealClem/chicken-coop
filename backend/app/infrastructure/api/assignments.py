from app.application.use_cases.create_assignment_usecase import CreateAssignmentUseCase
from app.application.use_cases.delete_assignment_usecase import DeleteAssignmentUseCase
from app.application.use_cases.get_assignments_usecase import GetAssignmentsUseCase
from app.application.use_cases.update_assignment_usecase import UpdateAssignmentUseCase
from app.infrastructure.db.mongo_assignment_repository import MongoAssignmentRepository
from fastapi import APIRouter, Depends
from app.domain.models.assignment import Assignment
from app.infrastructure.api.dependencies import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase


router = APIRouter(prefix="/assignments")

def get_assignment_repository(db: AsyncIOMotorDatabase = Depends(get_db)):
    return MongoAssignmentRepository(db)

def get_create_assignment_usecase(repo = Depends(get_assignment_repository)):
    return CreateAssignmentUseCase(repo)

@router.post("/")
async def create_assignment_usecase(assignment: Assignment, use_case = Depends(get_create_assignment_usecase)):
    return await use_case.execute(assignment)

def get_get_assignments_usecase(repo = Depends(get_assignment_repository)):
    return GetAssignmentsUseCase(repo)

@router.get("/")
async def get_assignments_usecase(month: int, year: int, use_case = Depends(get_get_assignments_usecase)):
    return await use_case.execute(month, year)

def get_delete_assignment_usecase(repo = Depends(get_assignment_repository)):
    return DeleteAssignmentUseCase(repo)

@router.delete("/{assignment_id}")
async def delete_assignment_usecase(assignment_id: str, use_case = Depends(get_delete_assignment_usecase)):
    await use_case.execute(assignment_id)
    return {"message": "Assignment deleted successfully"}

def get_update_assignment_usecase(repo = Depends(get_assignment_repository)):
    return UpdateAssignmentUseCase(repo)

@router.patch("/{assignment_id}")
async def update_assignment_usecase(assignment_id: str, updated_fields: Assignment, use_case = Depends(get_update_assignment_usecase)):
    return await use_case.execute(assignment_id, updated_fields)