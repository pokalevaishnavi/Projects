from sqlalchemy.orm import Session
from app.queries.task_queries import (
    CREATE_TASK,
    GET_ALL_TASKS,
    GET_TASKS_BY_USER,
    UPDATE_TASK_STATUS,
    DELETE_TASK
)


def create_task(db: Session, task_data: dict):
    result = db.execute(CREATE_TASK, task_data)
    db.commit()
    return result.fetchone()


def get_all_tasks(db: Session):
    result = db.execute(GET_ALL_TASKS)
    return result.fetchall()


def get_tasks_by_user(db: Session, user_id: int):
    result = db.execute(GET_TASKS_BY_USER, {"user_id": user_id})
    return result.fetchall()


def update_task_status(db: Session, task_id: int, status: str):
    result = db.execute(
        UPDATE_TASK_STATUS,
        {"task_id": task_id, "status": status}
    )
    db.commit()
    return result.fetchone()


def delete_task(db: Session, task_id: int):
    db.execute(DELETE_TASK, {"task_id": task_id})
    db.commit()
