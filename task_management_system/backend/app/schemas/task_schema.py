from pydantic import BaseModel
from datetime import date

class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_user: int
    due_date: date

class TaskUpdateStatus(BaseModel):
    status: str
