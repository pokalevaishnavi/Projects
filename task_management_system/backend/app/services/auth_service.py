from app.dao.user_dao import create_user, get_user_by_email
from app.core.security import hash_password, verify_password
from app.utils.jwt_utils import create_access_token


def register_user(db, user):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise Exception("User already exists")
    
    print("REGISTER password received:", user.password)

    hashed_pwd = hash_password(user.password)
    
    user_data = {
        "name": user.name,
        "email": user.email,
        "password": hashed_pwd,
        "role": user.role
    }

    create_user(db, user_data)
    return {"message": "User registered successfully"}



def login_user(db, user):
    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise Exception("Invalid credentials")

    if not verify_password(user.password, db_user.password):
        raise Exception("Invalid credentials")

    token = create_access_token({
        "user_id": db_user.id,
        "role": db_user.role
    })

    return token
