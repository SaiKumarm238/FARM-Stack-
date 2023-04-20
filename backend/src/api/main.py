from fastapi import FastAPI
from src.routers import todo
from src.routers import health

app = FastAPI(title="TO-DO API")

app.include_router(health.health_router)
app.include_router(todo.todo_router)
