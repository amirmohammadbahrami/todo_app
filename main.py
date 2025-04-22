from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel
from typing import Optional, List

# ایجاد اپلیکیشن FastAPI
app = FastAPI()

# اتصال به MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.todo_db
collection = db.tasks

# مدل برای ایجاد تسک جدید
class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# مدل خروجی با id
class TaskOut(TaskModel):
    id: str

# ایجاد endpoint برای دریافت تمام تسک‌ها
@app.get("/tasks", response_model=List[TaskOut])
async def get_tasks():
    tasks = []
    async for task in collection.find():
        tasks.append(TaskOut(
            id=str(task["_id"]),
            title=task["title"],
            description=task.get("description", ""),
            completed=task.get("completed", False)
        ))
    return tasks

# ایجاد endpoint برای اضافه کردن تسک جدید
@app.post("/tasks", response_model=TaskOut)
async def create_task(task: TaskModel):
    # تبدیل داده ورودی به دیکشنری و افزودن به MongoDB
    task_dict = task.dict()
    result = await collection.insert_one(task_dict)
    new_task = await collection.find_one({"_id": result.inserted_id})
    
    # بازگشت تسک جدید با id
    return TaskOut(
        id=str(new_task["_id"]),
        title=new_task["title"],
        description=new_task.get("description", ""),
        completed=new_task.get("completed", False)
    )

# ایجاد endpoint برای دریافت تسک خاص بر اساس شناسه
@app.get("/tasks/{id}", response_model=TaskOut)
async def get_task(id: str):
    # تبدیل id به ObjectId
    task = await collection.find_one({"_id": ObjectId(id)})
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return TaskOut(
        id=str(task["_id"]),
        title=task["title"],
        description=task.get("description", ""),
        completed=task.get("completed", False)
    )

# ایجاد endpoint برای به‌روزرسانی تسک خاص
@app.put("/tasks/{id}", response_model=TaskOut)
async def update_task(id: str, task: TaskModel):
    # تبدیل id به ObjectId
    updated_task = await collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": task.dict()},
        return_document=True
    )
    
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return TaskOut(
        id=str(updated_task["_id"]),
        title=updated_task["title"],
        description=updated_task.get("description", ""),
        completed=updated_task.get("completed", False)
    )

# ایجاد endpoint برای حذف تسک خاص
@app.delete("/tasks/{id}", response_model=TaskOut)
async def delete_task(id: str):
    # حذف تسک بر اساس id
    deleted_task = await collection.find_one_and_delete({"_id": ObjectId(id)})
    
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return TaskOut(
        id=str(deleted_task["_id"]),
        title=deleted_task["title"],
        description=deleted_task.get("description", ""),
        completed=deleted_task.get("completed", False)
    )
