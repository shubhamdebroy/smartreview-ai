from pydantic import BaseModel, Field

class ReviewRequest(BaseModel):
    review: str

class ReviewResponse(BaseModel):
    topics: list[str]
    sentiment: str
    confidence: float
    is_fake: bool
    suspicion_score: float
    flags: list[str]

class ReviewHistoryResponse(BaseModel):
    id: int
    review: str
    topics: list[str]
    sentiment: str
    confidence: float
    is_fake: bool
    suspicion_score: float
    flags: list[str]

class BatchReviewRequest(BaseModel):
    reviews: list[str] = Field(min_length=1, max_length=50)

class ReviewStatsResponse(BaseModel):
    total_reviews: int
    positive_reviews: int
    negative_reviews: int
    neutral_reviews: int
    fake_reviews: int