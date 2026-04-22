from backend.app.domain.models.user import User
from backend.app.domain.ports.user_repository import AbstractUserRepository


class GetUsersUseCase:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    async def execute(self) -> list[User]:
        return await self.user_repository.get_users()