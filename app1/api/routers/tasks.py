from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return TaskService(db).create_task(user.id, data)