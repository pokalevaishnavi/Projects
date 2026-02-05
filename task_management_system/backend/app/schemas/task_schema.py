from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int

class TaskUpdateStatus(BaseModel):
    status: str
