from sqlalchemy.orm import Session
from app.queries.task_queries import (
    CREATE_TASK,
    GET_ALL_TASKS,
    GET_TASKS_BY_USER,
    GET_TASK_BY_ID,
    UPDATE_TASK_STATUS,
    UPDATE_TASK_ASSIGNMENT,
    DELETE_TASK,
)


def create_task(db: Session, task_data: dict):
    result = db.execute(CREATE_TASK, task_data)
    db.commit()
    row = result.fetchone()
    return dict(row._mapping) if row else None


def get_all_tasks(db: Session):
    result = db.execute(GET_ALL_TASKS)
    return [dict(row._mapping) for row in result.fetchall()]


def get_tasks_by_user(db: Session, user_id: int):
    result = db.execute(GET_TASKS_BY_USER, {"user_id": user_id})
    return [dict(row._mapping) for row in result.fetchall()]


def get_task_by_id(db: Session, task_id: int):
    result = db.execute(GET_TASK_BY_ID, {"task_id": task_id})
    row = result.fetchone()
    return dict(row._mapping) if row else None


def update_task_status(db: Session, task_id: int, status: str):
    result = db.execute(
        UPDATE_TASK_STATUS,
        {"task_id": task_id, "status": status},
    )
    db.commit()
    row = result.fetchone()
    return dict(row._mapping) if row else None


def update_task_assignment(db: Session, task_id: int, user_id: int, due_date):
    result = db.execute(
        UPDATE_TASK_ASSIGNMENT,
        {"task_id": task_id, "user_id": user_id, "due_date": due_date},
    )
    db.commit()
    row = result.fetchone()
    return dict(row._mapping) if row else None


def delete_task(db: Session, task_id: int):
    db.execute(DELETE_TASK, {"task_id": task_id})
    db.commit()

