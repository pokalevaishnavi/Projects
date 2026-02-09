from sqlalchemy import text

CREATE_TASK = text("""
INSERT INTO tasks (title, description, status, user_id, due_date)
VALUES (
    :title,
    :description,
    'Backlog',
    NULLIF(:user_id, 0),
    :due_date
)
RETURNING *;
""")


GET_ALL_TASKS = text("""
SELECT * FROM tasks;
""")

GET_TASKS_BY_USER = text("""
SELECT * FROM tasks WHERE user_id = :user_id;
""")

GET_TASK_BY_ID = text("""
SELECT * FROM tasks WHERE id = :task_id;
""")


UPDATE_TASK_STATUS = text("""
UPDATE tasks
SET status = :status
WHERE id = :task_id
RETURNING *;
""")

UPDATE_TASK_ASSIGNMENT = text("""
UPDATE tasks
SET user_id = :user_id,
    due_date = :due_date
WHERE id = :task_id
RETURNING *;
""")

DELETE_TASK = text("""
DELETE FROM tasks WHERE id = :task_id;
""")
