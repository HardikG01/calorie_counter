from fastapi import FastAPI
from auth.router import router as auth_router
from calories.router import router as calorie_router
from app.database import create_db_and_tables

app = FastAPI(title="Calorie Tracker API")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(calorie_router, prefix="/calories", tags=["Calories"])
