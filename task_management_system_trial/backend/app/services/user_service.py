from app.dao.user_dao import get_all_users

def fetch_users_service(db):
    return get_all_users(db)