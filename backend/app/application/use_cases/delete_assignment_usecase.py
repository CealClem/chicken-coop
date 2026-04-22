from backend.app.domain.ports.assignment_repository import AbstractAssignmentRepository


class DeleteAssignmentUseCase:
    def __init__(self, assignment_repository: AbstractAssignmentRepository):
        self.assignment_repository = assignment_repository

    async def execute(self, assignment_id: str) -> None:
        await self.assignment_repository.delete_assignment(assignment_id)