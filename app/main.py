from fastapi import FastAPI
from app.routers.review import router
from app.database.database import initialize_database

app = FastAPI()

initialize_database()

app.include_router(router)


@app.get("/")
async def home():
    return {"message": "Welcome to the SmartReview API!"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }