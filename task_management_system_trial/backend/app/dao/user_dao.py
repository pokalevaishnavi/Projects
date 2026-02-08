from sqlalchemy.orm import Session
from sqlalchemy import text
from app.queries.user_queries import CREATE_USER, GET_USER_BY_EMAIL, GET_ALL_USERS
def create_user(db: Session, user_data: dict):
    result = db.execute(
        text(CREATE_USER),
        user_data
    )
    db.commit()
    return result.fetchone()



def get_user_by_email(db: Session, email: str):
    result = db.execute(
        text(GET_USER_BY_EMAIL),
        {"email": email}
    )
    return result.fetchone()

def get_all_users(db):
    result = db.execute(GET_ALL_USERS)
    return [dict(row._mapping) for row in result.fetchall()]