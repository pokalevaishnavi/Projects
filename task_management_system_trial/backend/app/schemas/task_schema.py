from datetime import date
from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int | None = None
    due_date: date | None = None


class TaskUpdateStatus(BaseModel):
    status: str



class TaskUpdateAssignment(BaseModel):
    user_id: Optional[int] = None
    due_date: Optional[date] = None

