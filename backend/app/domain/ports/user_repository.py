from abc import ABC, abstractmethod

from app.domain.models.user import User

class AbstractUserRepository(ABC):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        pass
    
    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    async def get_users(self) -> list[User]:
        pass

    @abstractmethod
    async def create_user(self, user_data: User) -> User:
        pass

    @abstractmethod
    async def update_user(self, user_id: str, updated_data: User) -> User:
        pass

    @abstractmethod
    async def delete_user(self, user_id: str) -> None:
        pass