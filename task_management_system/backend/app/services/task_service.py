from app.dao.task_dao import (
    create_task,
    get_all_tasks,
    get_tasks_by_user,
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



def fetch_tasks_service(db, token_data):
    role = token_data.get("role")
    user_id = token_data.get("user_id")

    if role == "admin":
        tasks = get_all_tasks(db)
    else:
        tasks = get_tasks_by_user(db, user_id)

    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        }
        for task in tasks
    ]



def update_task_status_service(db, task_id: int, new_status: str, token_data):
    if new_status not in ["Pending", "In Progress", "Completed"]:
        raise Exception("Invalid status")

    return update_task_status(db, task_id, new_status)


def delete_task_service(db, task_id: int):
    delete_task(db, task_id)
