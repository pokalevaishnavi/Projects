from sqlalchemy.orm import Session
from app.queries.user_queries import CREATE_USER, GET_USER_BY_EMAIL
from sqlalchemy import text

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