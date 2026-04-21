import datetime

from backend.app.domain.models.assignment import Assignment
from backend.app.domain.ports.assignment_repository import AbstractAssignmentRepository

from motor.motor_asyncio import AsyncIOMotorDatabase


class MongoAssignmentRepository(AbstractAssignmentRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.assignments

    async def create_assignment(self, assignment: Assignment) -> Assignment:
        result = await self.collection.insert_one(assignment.model_dump())
        assignment.id = str(result.inserted_id)
        return assignment

    async def get_assignment_by_id(self, assignment_id: str) -> Assignment | None:
        assignment = await self.collection.find_one({"_id": assignment_id})
        if assignment:
            return Assignment(**assignment)
        return None

    async def get_assignments(self, month: int, year: int) -> list[Assignment]:
        start = datetime.date(year, month, 1)
        end = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        assignments = await self.collection.find({"date": {"$gte": start, "$lt": end}}).to_list(length=None)
        return [Assignment(**assignment) for assignment in assignments]

    async def update_assignment(self, assignment_id: str, updated_fields: Assignment) -> Assignment:
        result = await self.collection.update_one(
            {"_id": assignment_id},
            {"$set": updated_fields.model_dump()}
        )
        assert result.modified_count > 0
        return await self.get_assignment_by_id(assignment_id)


    async def delete_assignment(self, assignment_id: str) -> None:
        result = await self.collection.delete_one({"_id": assignment_id})
        assert result.deleted_count == 1