import httpx
from fuzzywuzzy import process
from app.config import settings

def fetch_calories(food_name: str) -> float:
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        "query": food_name,
        "api_key": settings.USDA_API_KEY,
        "pageSize": 15
    }

    response = httpx.get(url, params=params)
    response.raise_for_status()

    results = response.json().get("foods", [])
    if not results:
        raise Exception("Food not found")

    names = [f["description"] for f in results]
    best_match = process.extractOne(food_name, names)
    best_food = next((f for f in results if f["description"] == best_match[0]), None)

    for nutrient in best_food.get("foodNutrients", []):
        if "Energy" in nutrient["nutrientName"] and nutrient.get("unitName") in ["KCAL", "kcal"]:
            return nutrient["value"]  # per 100g or per serving based on USDA data

    raise Exception("Calorie data not found")
