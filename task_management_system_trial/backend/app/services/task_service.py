from app.dao.task_dao import (
    create_task,
    get_all_tasks,
    get_tasks_by_user,
    get_task_by_id,
    update_task_status,
    update_task_assignment,
    delete_task,
)


# Canonical set of allowed task statuses used by the frontend Kanban board
ALLOWED_STATUSES = {"Backlog", "In Progress", "Review", "Done"}


def create_task_service(db, task):
    """Create a new task that always starts in Backlog."""
    task_data = task.model_dump() 
    task_data["status"] = "Backlog"
    return create_task(db, task_data)


def fetch_tasks_service(db):
    return get_all_tasks(db)


def fetch_tasks_by_user_service(db, user_id):
    return get_tasks_by_user(db, user_id)


def update_task_status_service(db, task_id: int, new_status: str):
    """Update a task status, allowing movement between any of the allowed columns."""
    task = get_task_by_id(db, task_id)

    if not task:
        raise Exception("Task not found")

    if new_status not in ALLOWED_STATUSES:
        raise Exception(f"Invalid status: {new_status}")

    return update_task_status(db, task_id, new_status)


def update_task_assignment_service(db, task_id: int, user_id: int | None, due_date):
    task = get_task_by_id(db, task_id)

    if not task:
        raise Exception("Task not found")

    # convert NA to default unassigned user (1)
    if user_id is None:
        user_id = 1

    return update_task_assignment(db, task_id, user_id, due_date)

def delete_task_service(db, task_id: int):
    delete_task(db, task_id)
