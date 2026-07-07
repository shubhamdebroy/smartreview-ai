import logging

from fastapi import APIRouter, Query, HTTPException

from app.schemas.review_schema import (
    ReviewRequest,
    ReviewResponse,
    ReviewHistoryResponse,
    BatchReviewRequest,
    ReviewStatsResponse
)
from app.services.review_services import (
    analyse_review,
    get_review_history,
    analyse_batch,
    get_review_stats
)


logger = logging.getLogger(__name__)


router = APIRouter(prefix="/reviews", tags=["Review"])


@router.post("/analyse", response_model=ReviewResponse)
async def analyse(request: ReviewRequest):
    try:
        response = analyse_review(request)
        return response
    except Exception:
        logger.exception("Review analysis failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to analyse review"
        )


@router.get("/history", response_model=list[ReviewHistoryResponse])
async def get_history(limit: int = Query(default=10, ge=1, le=100)):
    try:
        reviews = get_review_history(limit)
        return reviews
    except Exception:
        logger.exception("Review history retrieval failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve review history"
        )


@router.post("/batch", response_model=list[ReviewResponse])
async def batch_analyse(batch_requests: BatchReviewRequest):
    try:
        responses = analyse_batch(batch_requests)
        return responses
    except Exception:
        logger.exception("Batch review analysis failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to analyse batch reviews"
        )


@router.get("/stats", response_model=ReviewStatsResponse)
async def get_stats():
    try:
        statistics = get_review_stats()
        return statistics
    except Exception:
        logger.exception("Review statistics retrieval failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve review statistics"
        )