CREATE_TASK = """
INSERT INTO tasks (title, description, assigned_user, status, due_date, created_date)
VALUES (:title, :description, :assigned_user, 'Pending', :due_date, NOW())
RETURNING *;
"""

GET_ALL_TASKS = """
SELECT * FROM tasks;
"""

GET_TASKS_BY_USER = """
SELECT * FROM tasks WHERE assigned_user = :user_id;
"""

UPDATE_TASK_STATUS = """
UPDATE tasks
SET status = :status
WHERE id = :task_id
RETURNING *;
"""

DELETE_TASK = """
DELETE FROM tasks WHERE id = :task_id;
"""
