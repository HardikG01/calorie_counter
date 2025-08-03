from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import settings
from app.database import SessionLocal, get_db
from auth.models import User
from calories.models import CalorieRequest, CalorieResponse
from calories.services import log_calorie

router = APIRouter(prefix="/calories", tags=["Calories"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")  # Expecting email in "sub"
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/get-calories", response_model=CalorieResponse)
def add_calories(request: CalorieRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    data = log_calorie(user.id, request, db)
    return data
