from sqlalchemy.orm import Session
from calories.models import CalorieEntry

def add_calorie_entry(user_id: int, food_name: str, servings: float, total_calories: float, db: Session) -> CalorieEntry:
    entry = CalorieEntry(
        user_id=user_id,
        food_name=food_name,
        servings=servings,
        calories=total_calories
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)  # To get generated ID if needed
    return entry
