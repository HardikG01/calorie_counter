# 🥗 Calorie Tracker API

A modern FastAPI backend to track calories consumed via food entries. It integrates with the USDA FoodData Central API to fetch calorie information and supports user authentication using JWT tokens.

## ⚙️ Setup Instructions

1. **Clone the repo:**
git clone https://github.com/your-username/calorie-tracker-api.git
cd calorie-tracker-api

2. **Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
pip install -r requirements.txt

4. **Configure your .env file:**
DATABASE_URL=sqlite:///./calories.db  # or use PostgreSQL
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
USDA_API_KEY=your-usda-api-key

5. **Run the application:**
uvicorn main:app --reload

6. **Access API docs:**
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc