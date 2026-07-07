from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME)

def analyse_sentiment(review: str):
    result = sentiment_pipeline(
    review,
    truncation=True,
    max_length=512
    )[0]
    return {
        "sentiment": result["label"].lower(),
        "confidence": result["score"]
    }
