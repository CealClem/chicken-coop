from app.domain.models.assignment import Assignment
from app.domain.ports.assignment_repository import AbstractAssignmentRepository


class GetAssignmentsUseCase:
    def __init__(self, assignment_repository: AbstractAssignmentRepository):
        self.assignment_repository = assignment_repository

    async def execute(self, month: int, year: int) -> list[Assignment]:
        return await self.assignment_repository.get_assignments(month, year)