from fastapi import APIRouter, Body, Request, HTTPException, status
from src.models.models import TaskModel, UpdateTaskModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.database import database

todo_router = APIRouter(tags=["TODO"], prefix="/task")


@todo_router.get("/", response_description="List all Tasks")
async def list_tasks():
    task = await database.get_tasks_async()
    return task


@todo_router.post("/", response_description="Add new Task")
async def create_task(task: TaskModel = Body(...)):
    task = jsonable_encoder(task)
    created_task = await database.create_task_async(task)
    return JSONResponse(status_code= status.HTTP_201_CREATED, content=created_task)


@todo_router.get("/{id}", response_description="Get a single task")
async def show_task(id: str):
    task = await database.get_task_by_id_async(id)

    if task is not None:
        return task
        
    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@todo_router.put("/{id}", response_description="Update a task")
async def update_task(id: str, task: UpdateTaskModel = Body(...)):
    task = {k: v for k, v in task.dict().items() if v is not None}

    if len(task) >= 1:
        update_result = await database.update_task_by_id_async(id, task)

        if update_result.modified_count == 1:
            updated_task = await database.get_task_by_id_async(id)

            if updated_task is not None:
                return updated_task

    existing_task = await database.get_task_by_id_async(id)

    if existing_task is not None:
        return existing_task

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@todo_router.delete("/{id}", response_description="Delete Task")
async def delete_task(id: str):
    delete_result = await database.delete_task_by_id_async(id)

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)

    raise HTTPException(status_code=404, detail=f"Task {id} not found")