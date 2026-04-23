from app.domain.models.assignment import Assignment
from app.domain.ports.assignment_repository import AbstractAssignmentRepository


class CreateAssignmentUseCase:
    def __init__(self, assignment_repository: AbstractAssignmentRepository):
        self.assignment_repository = assignment_repository

    async def execute(self, assignment_data: Assignment) -> Assignment:
        # TODO: Add validation logic here (e.g., check for overlapping assignments, validate date formats, etc.)
        return await self.assignment_repository.create_assignment(assignment_data)
