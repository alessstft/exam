from typing import Optional

from sqlalchemy.orm import Session

from app1.models.task import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, owner_id: int, title: str, description: str = "") -> Task:
        task = Task(owner_id=owner_id, title=title, description=description, status="new")
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def list_by_owner(self, owner_id: int) -> list[Task]:
        return self.db.query(Task).filter(Task.owner_id == owner_id).all()

    def update(self, task: Task) -> Task:
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()
