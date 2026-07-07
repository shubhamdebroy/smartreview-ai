from app.utils.sentiment_analyzer import analyse_sentiment


evaluation_dataset = [
    # Positive reviews
    {
        "review": "The battery life is excellent and lasts all day.",
        "expected": "positive"
    },
    {
        "review": "Amazing product with great build quality.",
        "expected": "positive"
    },
    {
        "review": "The phone performs smoothly and apps open very quickly.",
        "expected": "positive"
    },
    {
        "review": "I am very satisfied with this purchase.",
        "expected": "positive"
    },
    {
        "review": "The delivery was fast and the product arrived in perfect condition.",
        "expected": "positive"
    },
    {
        "review": "Excellent value for the price.",
        "expected": "positive"
    },
    {
        "review": "The customer support team was helpful and resolved my issue quickly.",
        "expected": "positive"
    },
    {
        "review": "The camera quality is fantastic and the photos look beautiful.",
        "expected": "positive"
    },
    {
        "review": "This laptop works perfectly for my daily tasks.",
        "expected": "positive"
    },
    {
        "review": "The product exceeded my expectations.",
        "expected": "positive"
    },

    # Negative reviews
    {
        "review": "The battery drains extremely fast and barely lasts a few hours.",
        "expected": "negative"
    },
    {
        "review": "Terrible product with very poor build quality.",
        "expected": "negative"
    },
    {
        "review": "The phone is slow and constantly freezes.",
        "expected": "negative"
    },
    {
        "review": "I regret buying this product.",
        "expected": "negative"
    },
    {
        "review": "The delivery was late and the package arrived damaged.",
        "expected": "negative"
    },
    {
        "review": "The product is overpriced and not worth the money.",
        "expected": "negative"
    },
    {
        "review": "Customer support was unhelpful and did not solve my problem.",
        "expected": "negative"
    },
    {
        "review": "The camera quality is awful and the images are blurry.",
        "expected": "negative"
    },
    {
        "review": "This laptop crashes frequently and is frustrating to use.",
        "expected": "negative"
    },
    {
        "review": "The product failed to meet my expectations.",
        "expected": "negative"
    },

    # Neutral reviews
    {
        "review": "The phone has a 6.5 inch display.",
        "expected": "neutral"
    },
    {
        "review": "The package arrived on Monday.",
        "expected": "neutral"
    },
    {
        "review": "The laptop includes a charging adapter.",
        "expected": "neutral"
    },
    {
        "review": "The product is available in three colors.",
        "expected": "neutral"
    },
    {
        "review": "The battery capacity is 5000 mAh.",
        "expected": "neutral"
    },
    {
        "review": "The device weighs 180 grams.",
        "expected": "neutral"
    },
    {
        "review": "The box contains the phone and a USB cable.",
        "expected": "neutral"
    },
    {
        "review": "The product was released last year.",
        "expected": "neutral"
    },
    {
        "review": "The laptop has 16 GB of RAM.",
        "expected": "neutral"
    },
    {
        "review": "The phone uses a USB Type-C port.",
        "expected": "neutral"
    }
]


correct_predictions = 0

print("\nSmartReview Sentiment Accuracy Evaluation")
print("=" * 50)

for index, sample in enumerate(evaluation_dataset, start=1):
    result = analyse_sentiment(sample["review"])

    predicted = result["sentiment"]
    expected = sample["expected"]

    is_correct = predicted == expected

    if is_correct:
        correct_predictions += 1

    print(f"\nSample {index}")
    print(f"Review:    {sample['review']}")
    print(f"Expected:  {expected}")
    print(f"Predicted: {predicted}")
    print(f"Correct:   {is_correct}")


total_samples = len(evaluation_dataset)

accuracy = (correct_predictions / total_samples) * 100


print("\n" + "=" * 50)
print("Evaluation Summary")
print("=" * 50)
print(f"Total samples:       {total_samples}")
print(f"Correct predictions: {correct_predictions}")
print(f"Incorrect predictions: {total_samples - correct_predictions}")
print(f"Accuracy:            {accuracy:.2f}%")