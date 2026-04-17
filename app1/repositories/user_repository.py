from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app1.core.security import hash_password
from app1.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.query(User).filter(User.username == username).first()

    def get_by_login(self, login: str) -> Optional[User]:
        return self.db.query(User).filter(or_(User.email == login, User.username == login)).first()

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def list_all(self) -> list[User]:
        return self.db.query(User).all()

    def create(self, email: str, username: str, phone: str, password: str, role: str = "user") -> User:
        user = User(
            email=email,
            username=username,
            phone=phone,
            hashed_password=hash_password(password),
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
