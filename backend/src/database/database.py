import os
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient(os.environ["MongoDBServer"])
database = client[os.environ["MongoDBDatabase"]]

ToDoCollection = database["ToDo"]

async def get_tasks_async():
    return await ToDoCollection.find().to_list(length=100)

async def create_task_async(task):
    new_task = await ToDoCollection.insert_one(task)
    created_task = await ToDoCollection.find_one({"_id":new_task.inserted_id})
    return created_task

async def get_task_by_id_async(id):
    return await ToDoCollection.find_one({"_id": id})

async def update_task_by_id_async(id, task):
    return await ToDoCollection.update_one({"_id": id}, {"$set": task})

async def delete_task_by_id_async(id):
    return await ToDoCollection.delete_one({"_id": id})