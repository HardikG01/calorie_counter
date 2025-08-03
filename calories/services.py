from sqlalchemy.orm import Session
from calories.models import CalorieRequest
from calories.usda import fetch_calories
from utils.cache import cache
from calories.dal import add_calorie_entry

def log_calorie(user_id: int, req: CalorieRequest, db: Session):
    key = f"{req.food_name.lower()}_cal"
    
    if key in cache:
        calories_per_serving = cache[key]
    else:
        calories_per_serving = fetch_calories(req.food_name)
        cache[key] = calories_per_serving

    total_calories = round(calories_per_serving * req.servings, 2)

    # Call the DAL to persist the data
    add_calorie_entry(user_id, req.food_name, req.servings, total_calories, db)

    return {
        "food_name": req.food_name,
        "servings": req.servings,
        "calories_per_serving": calories_per_serving,
        "total_calories": total_calories,
        "source": "USDA FoodData Central"
    }
