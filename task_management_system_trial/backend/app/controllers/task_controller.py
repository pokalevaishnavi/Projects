from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskUpdateStatus, TaskUpdateAssignment
from app.services.task_service import (
    create_task_service,
    fetch_tasks_service,
    update_task_status_service,
    update_task_assignment_service,
    delete_task_service,
    fetch_tasks_by_user_service,
    
)
from app.core.database import SessionLocal
from app.utils.jwt_utils import verify_token
from app.core.security import admin_required

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    # token_data: dict = Depends(admin_required)
):
    return create_task_service(db, task)


@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    # token_data: dict = Depends(verify_token),
):
    return fetch_tasks_service(db)

@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}")
def get_my_tasks(
    user_id: int,
    db: Session = Depends(get_db),
    # token_data: dict = Depends(verify_token)
):
    # user_id = token_data["user_id"]
    return fetch_tasks_by_user_service(db, user_id)


@router.patch("/{task_id}/status")
def update_status(
    task_id: int,
    status: TaskUpdateStatus,
    db: Session = Depends(get_db),
    # token_data: dict = Depends(verify_token),
):
    try:
        return update_task_status_service(db, task_id, status.status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{task_id}/assignment")
def update_assignment(
    task_id: int,
    payload: TaskUpdateAssignment,
    db: Session = Depends(get_db),
    # token_data: dict = Depends(verify_token),
):
    try:
        return update_task_assignment_service(
            db, task_id, payload.user_id, payload.due_date
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    # token_data: dict = Depends(admin_required),
):
    delete_task_service(db, task_id)
    return {"message": "Task deleted successfully"}
