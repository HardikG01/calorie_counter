from sqlalchemy.orm import Session
from auth.models import User
from utils.hashing import Hasher

class AuthDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, first_name: str, last_name: str, email: str, password: str):
        hashed_pw = Hasher.get_password_hash(password)
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            hashed_password=hashed_pw
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
