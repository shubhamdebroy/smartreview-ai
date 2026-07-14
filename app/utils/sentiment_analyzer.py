from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Lazy-loaded pipeline
sentiment_pipeline = None


def get_pipeline():
    global sentiment_pipeline

    if sentiment_pipeline is None:
        print("Loading sentiment model...")
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model=MODEL_NAME
        )
        print("Sentiment model loaded successfully!")

    return sentiment_pipeline


def analyse_sentiment(review: str):
    pipe = get_pipeline()

    result = pipe(
        review,
        truncation=True,
        max_length=512
    )[0]

    return {
        "sentiment": result["label"].lower(),
        "confidence": result["score"]
    }