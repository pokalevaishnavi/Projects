from sqlalchemy import text

CREATE_USER = text("""
INSERT INTO users (name, email, password)
VALUES (:name, :email, :password)
RETURNING *;
""")

GET_USER_BY_EMAIL = text("""
SELECT * FROM users
WHERE email = :email;
""")

GET_ALL_USERS = text("""
SELECT id, name
FROM users
ORDER BY id;
""")