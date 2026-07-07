import logging

from app.schemas.review_schema import ReviewRequest, ReviewResponse, BatchReviewRequest
from app.repositories.review_repository import save_review, get_all_reviews, get_review_statistics
from app.utils.sentiment_analyzer import analyse_sentiment
from app.utils.fake_review_detector import detect_fake_review
from app.utils.topic_extractor import extract_topics


logger = logging.getLogger(__name__)


def analyse_review(request: ReviewRequest):
    sentiment_analysis = analyse_sentiment(request.review)
    fake_analysis = detect_fake_review(request.review)
    topics = extract_topics(request.review)

    sentiment = sentiment_analysis["sentiment"]
    confidence = sentiment_analysis["confidence"]
    is_fake = fake_analysis["is_fake"]
    suspicion_score = fake_analysis["suspicion_score"]
    flags = fake_analysis["flags"]

    save_review(
        request.review,
        topics,
        sentiment,
        confidence,
        is_fake,
        suspicion_score,
        flags
    )

    logger.info(
        "Review analysed successfully: sentiment=%s, is_fake=%s",
        sentiment,
        is_fake
    )

    return ReviewResponse(
        topics=topics,
        sentiment=sentiment,
        confidence=confidence,
        is_fake=is_fake,
        suspicion_score=suspicion_score,
        flags=flags
    )


def get_review_history(limit: int):
    reviews = get_all_reviews(limit)
    return reviews


def analyse_batch(batch_requests: BatchReviewRequest):
    responses = []

    for review in batch_requests.reviews:
        review_request = ReviewRequest(review=review)
        response = analyse_review(review_request)
        responses.append(response)

    logger.info(
        "Batch analysis completed successfully: review_count=%s",
        len(responses)
    )

    return responses


def get_review_stats():
    statistics = get_review_statistics()
    return statistics