from sqlalchemy.orm import Session
from app.models.user_model import User
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def register_user(db: Session, user):
    # 1️⃣ Check existing user
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise Exception("User already exists")

    # 2️⃣ Hash password
    hashed_password = hash_password(user.password)

    new_user = User(
    name=user.name,
    email=user.email,
    password=hashed_password,
    role=user.role,
)


    # 4️⃣ Save
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "email": new_user.email,
        "role": new_user.role,
    }



def login_user(db: Session, user):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise Exception("Invalid credentials")

    if not verify_password(user.password, db_user.password):
        raise Exception("Invalid credentials")

    return "FAKE_TOKEN_FOR_NOW"
