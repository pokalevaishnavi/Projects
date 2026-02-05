from sqlalchemy import text

CREATE_TASK = text("""
INSERT INTO tasks (title, description, status, user_id)
VALUES (:title, :description, 'Pending', :user_id)
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

DELETE_TASK = text("""
DELETE FROM tasks WHERE id = :task_id;
""")
