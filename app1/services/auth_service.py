from fastapi import HTTPException
from sqlalchemy.orm import Session

from app1.core.security import verify_password
from app1.repositories.user_repository import UserRepository
from app1.schemas.user import RegisterRequest


class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def register_user(self, data: RegisterRequest):
        if self.user_repo.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already in use")
        if self.user_repo.get_by_username(data.username):
            raise HTTPException(status_code=400, detail="Username already in use")

        return self.user_repo.create(
            email=data.email,
            username=data.username,
            phone=data.phone,
            password=data.password,
        )

    def authenticate_user(self, login: str, password: str):
        user = self.user_repo.get_by_login(login)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
