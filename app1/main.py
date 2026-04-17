from fastapi import FastAPI

from app1.api.routers import admin, auth, tasks
from app1.core.database import Base, engine

# app = FastAPI(title="Task API")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.on_event("startup")
def on_startup() -> None:
    import app1.models.task  # noqa: F401
    import app1.models.user  # noqa: F401

    Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(admin.router)
