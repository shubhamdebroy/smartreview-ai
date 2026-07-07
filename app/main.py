from fastapi import FastAPI
from app.routers.review import router
from app.database.database import initialize_database

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
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