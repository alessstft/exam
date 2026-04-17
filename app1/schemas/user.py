import re
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class RegisterRequest(BaseModel):
    email: str
    username: str
    phone: str
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, value):
            raise ValueError("Invalid email")
        return value

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,19}$"
        if not re.match(pattern, value):
            raise ValueError("Username must start with a letter and be 3-20 chars long")
        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        pattern = r"^\+7-\d{3}-\d{3}-\d{2}-\d{2}$"
        if not re.match(pattern, value):
            raise ValueError("Phone must match +7-900-123-45-67")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 chars")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must include an uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must include a lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must include a digit")
        return value


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: int
    email: str
    username: str
    phone: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
