from pydantic import BaseModel, Field, field_validator

class ReviewRequest(BaseModel):
    review: str

    @field_validator("review")
    @classmethod
    def validate_review(cls, value: str):
        if not value.strip():
            raise ValueError("Review cannot be empty or whitespace")
        
        return value


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

    @field_validator("reviews")
    @classmethod
    def validate_reviews(cls, values: list[str]):
        if any(not review.strip() for review in values):
            raise ValueError("Batch reviews must not contain empty reviews")

        return values

class ReviewStatsResponse(BaseModel):
    total_reviews: int
    positive_reviews: int
    negative_reviews: int
    neutral_reviews: int
    fake_reviews: int