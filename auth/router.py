from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.models import UserCreate, UserLogin, Token
from auth.services import AuthService
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=Token)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.register_user(user_data)
    return service.login_user(user.email, user_data.password)

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login_user(user_data.email, user_data.password)
