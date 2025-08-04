from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from auth.dal import AuthDAL
from auth.models import UserCreate
from utils.hashing import Hasher
from utils.jwt import create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.dal = AuthDAL(db)

    def register_user(self, user_data: UserCreate):
        if self.dal.get_user_by_email(user_data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        return self.dal.create_user(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password
        )

    def login_user(self, email: str, password: str):
        user = self.dal.get_user_by_email(email)
        if not user or not Hasher.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        token = create_access_token(user.email)
        return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
    }