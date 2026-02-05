from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from app.utils.jwt_utils import verify_token

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def admin_required(token_data: dict = Depends(verify_token)):
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return token_data


def employee_required(token_data: dict = Depends(verify_token)):
    if token_data.get("role") not in ["employee", "admin"]:
        raise HTTPException(status_code=403, detail="Employee access required")
    return token_data
