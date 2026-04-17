from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app1.api.deps import get_current_admin, get_db
from app1.repositories.user_repository import UserRepository
from app1.schemas.user import UserOut

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db), _=Depends(get_current_admin)):
    return UserRepository(db).list_all()
