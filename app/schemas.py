from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None  # ← manejo de fecha

class TaskCreate(TaskBase):
    title: str  # title obligatorio al crear

class TaskUpdate(TaskBase):
    completed: Optional[bool] = None  # parcialidad también en `completed`

class TaskOut(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
