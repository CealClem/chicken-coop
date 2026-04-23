from abc import ABC, abstractmethod

from app.domain.models.assignment import Assignment

class AbstractAssignmentRepository(ABC):
    @abstractmethod
    async def get_assignments(self, month: int, year: int) -> list[Assignment]:
        pass

    @abstractmethod
    async def create_assignment(self, assignment_data: Assignment) -> Assignment:
        pass

    @abstractmethod
    async def get_assignment_by_id(self, assignment_id: str) -> Assignment:
        pass

    @abstractmethod
    async def update_assignment(self, assignment_id: str, updated_data: Assignment) -> Assignment:
        pass

    @abstractmethod
    async def delete_assignment(self, assignment_id: str) -> None:
        pass