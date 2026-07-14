import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.review import router
from app.database.database import initialize_database
from app.utils.sentiment_analyzer import get_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title="SmartReview API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "https://smartreviewai.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logger.info("SmartReview application startup initiated")

    initialize_database()
    logger.info("SmartReview database initialized successfully")

    logger.info("Loading sentiment model...")
    get_pipeline()
    logger.info("Sentiment model loaded successfully!")

    logger.info("SmartReview application ready")


app.include_router(router)


@app.get("/")
async def home():
    return {"message": "Welcome to the SmartReview API!"}


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }