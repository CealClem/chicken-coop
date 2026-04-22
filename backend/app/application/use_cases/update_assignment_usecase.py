from backend.app.domain.models.assignment import Assignment
from backend.app.domain.ports.assignment_repository import AbstractAssignmentRepository


class UpdateAssignmentUseCase:
    def __init__(self, assignment_repository: AbstractAssignmentRepository):
        self.assignment_repository = assignment_repository

    async def execute(self, assignment_id: str, updated_fields: Assignment) -> Assignment:
        return await self.assignment_repository.update_assignment(assignment_id, updated_fields)