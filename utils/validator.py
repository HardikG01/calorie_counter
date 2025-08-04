import re
from fastapi import HTTPException, status

def validate_dish_name(food_name: str):
    if not food_name.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Dish name cannot be empty."
        )

    if len(food_name) < 2:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Dish name must be at least 2 characters long."
        )

    if len(food_name) > 100:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Dish name is too long. Maximum allowed is 100 characters."
        )

    if re.search(r'\d', food_name):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Dish name should not contain numbers."
        )

    if re.search(r'[^a-zA-Z\s]', food_name):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Dish name should not contain special characters."
        )

def validate_servings(servings: float):
    if servings <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Servings must be greater than zero."
        )
    
    if servings > 100:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Servings value is too large. Must be less than or equal to 100."
        )
