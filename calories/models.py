from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base
from pydantic import BaseModel
from typing import Optional


# SQLAlchemy ORM model
class CalorieEntry(Base):
    __tablename__ = "calories"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    food_name = Column(String, nullable=False)
    servings = Column(Float, nullable=False)
    calories = Column(Float, nullable=False)


# Pydantic schema for request
class CalorieRequest(BaseModel):
    food_name: str
    servings: float


# Pydantic schema for response
class CalorieResponse(BaseModel):
    food_name: str
    servings: float
    calories_per_serving: float
    total_calories: float
    source: str

    class Config:
        orm_mode = True  # Enables conversion from ORM model to response
