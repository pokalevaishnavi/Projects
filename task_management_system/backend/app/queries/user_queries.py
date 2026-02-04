CREATE_USER = """
INSERT INTO users (name, email, password, role)
VALUES (:name, :email, :password, :role)
RETURNING id, email, role;
"""

GET_USER_BY_EMAIL = """
SELECT * FROM users WHERE email = :email;
"""
