from backend.app.domain.models.user import User
from backend.app.domain.ports.user_repository import AbstractUserRepository
from passlib.context import CryptContext


class CreateUserUsecase:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    async def execute(self, first_name: str, last_name: str, email: str, password: str) -> User:
        existing_user = await self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("Email already in use")
        
        hashed_password = self.pwd_context.hash(password)  
        new_user = User(first_name=first_name, last_name=last_name, email=email, password_hash=hashed_password)
        return await self.user_repository.create_user(new_user)