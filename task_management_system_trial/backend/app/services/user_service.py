from sqlalchemy.orm import Session
from app.models.user_model import User

def fetch_users_service(db: Session):
    return db.query(User).all()
