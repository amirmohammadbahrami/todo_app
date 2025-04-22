from bson import ObjectId
from database import task_collection

def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task.get("description", ""),
        "completed": task["completed"],
    }

# Create
async def add_task(task_data: dict) -> dict:
    task = await task_collection.insert_one(task_data)
    new_task = await task_collection.find_one({"_id": task.inserted_id})
    return task_helper(new_task)

# Read All
async def get_tasks():
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_helper(task))
    return tasks

# Read One
async def get_task(id: str) -> dict:
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        return task_helper(task)

# Update
async def update_task(id: str, data: dict):
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        await task_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

# Delete
async def delete_task(id: str):
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        await task_collection.delete_one({"_id": ObjectId(id)})
        return True
