from app.domain.models.user import User
from app.domain.ports.user_repository import AbstractUserRepository
import hashlib
import base64
import bcrypt


class CreateUserUsecase:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    def hash_password(self, password: str) -> str:
        # SHA-256 the password first, then bcrypt the result
        sha256_hash = hashlib.sha256(password.encode()).digest()
        b64_hash = base64.b64encode(sha256_hash)
        return bcrypt.hashpw(b64_hash, bcrypt.gensalt()).decode()

    async def execute(self, first_name: str, last_name: str, email: str, password: str) -> User:
        existing_user = await self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("Email already in use")
        
        hashed_password = self.hash_password(password)  
        new_user = User(first_name=first_name, last_name=last_name, email=email, password_hash=hashed_password)
        return await self.user_repository.create_user(new_user)