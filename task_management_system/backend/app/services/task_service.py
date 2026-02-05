from app.dao.task_dao import (
    create_task,
    get_all_tasks,
    get_tasks_by_user,
    get_task_by_id,
    update_task_status,
    delete_task
)

VALID_STATUS_FLOW = {
    "Pending": "In Progress",
    "In Progress": "Completed"
}


def create_task_service(db, task):
    task_data = task.dict()
    task_data["status"] = "Pending"
    return create_task(db, task_data)

def fetch_tasks_service(db):
    return get_all_tasks(db)

# def fetch_tasks_service(db, token_data):
#     role = token_data.get("role")
#     user_id = token_data.get("user_id")

#     if role == "admin":
#         tasks = get_all_tasks(db)
#     else:
#         tasks = get_tasks_by_user(db, user_id)

#     return [
#         {
#             "id": task.id,
#             "title": task.title,
#             "description": task.description,
#             "status": task.status
#         }
#         for task in tasks
#     ]



VALID_STATUS_FLOW = {
    "Pending": "In Progress",
    "In Progress": "Completed"
}

def update_task_status_service(db, task_id: int, new_status: str, token_data):
    task = get_task_by_id(db, task_id)

    if not task:
        raise Exception("Task not found")

    current_status = task["status"]

    if current_status not in VALID_STATUS_FLOW:
        raise Exception("Task already completed")

    if VALID_STATUS_FLOW[current_status] != new_status:
        raise Exception(
            f"Invalid status transition: {current_status} → {new_status}"
        )

    return update_task_status(db, task_id, new_status)


def delete_task_service(db, task_id: int):
    delete_task(db, task_id)
