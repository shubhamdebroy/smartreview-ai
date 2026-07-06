TOPIC_KEYWORDS = {
    "battery": ["battery", "charge", "charging", "power"],
    "delivery": ["delivery", "shipping", "arrived", "courier"],
    "price": ["price", "expensive", "cheap", "cost", "value"],
    "quality": ["quality", "durable", "build", "broken", "material"],
    "performance": ["performance", "fast", "slow", "lag", "speed"],
    "support": ["support", "service", "customer care", "replacement"]
}

def extract_topics(review: str) -> list[str]:
    review_lower = review.lower()
    topics =[]
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword in review_lower for keyword in keywords):
            topics.append(topic)
    return topics