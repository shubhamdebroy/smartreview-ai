from transformers import pipeline

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

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


def analyze_sentiment(review: str):
    classifier = get_pipeline()

    result = classifier(review)[0]

    sentiment = result["label"].lower()

    if sentiment == "positive":
        sentiment = "positive"
    elif sentiment == "negative":
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "sentiment": sentiment,
        "confidence": round(float(result["score"]), 4),
    }