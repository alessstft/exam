import json
from fastapi import HTTPException
from app.repositories.task_repository import TaskRepository
from app.utils.redis_client import redis_client

class TaskService:
    def __init__(self, db):
        self.repo = TaskRepository(db)

    def _cache_key(self, user_id):
        return f"user:{user_id}:tasks"

    def _invalidate(self, user_id):
        if redis_client:
            redis_client.delete(self._cache_key(user_id))

    def create_task(self, user_id, data):
        task = self.repo.create(user_id, data.title, data.description or "")
        self._invalidate(user_id)
        return task

    def list_tasks(self, user_id):
        if redis_client:
            cached = redis_client.get(self._cache_key(user_id))
            if cached:
                return json.loads(cached)

        tasks = self.repo.list_by_owner(user_id)
        result = [t.__dict__ for t in tasks]

        if redis_client:
            redis_client.setex(self._cache_key(user_id), 60, json.dumps(result, default=str))

        return result