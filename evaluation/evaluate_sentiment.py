from app.utils.sentiment_analyzer import analyze_sentiment


evaluation_dataset = [
    # -------------------------
    # Positive Reviews (15)
    # -------------------------
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
    {
        "review": "The display is bright and the speakers sound excellent.",
        "expected": "positive"
    },
    {
        "review": "Setup was quick and everything worked exactly as expected.",
        "expected": "positive"
    },
    {
        "review": "The software is easy to use and runs flawlessly.",
        "expected": "positive"
    },
    {
        "review": "Very reliable product with impressive performance.",
        "expected": "positive"
    },
    {
        "review": "I would definitely recommend this product to others.",
        "expected": "positive"
    },

    # -------------------------
    # Negative Reviews (15)
    # -------------------------
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
    {
        "review": "The display flickers constantly and is difficult to read.",
        "expected": "negative"
    },
    {
        "review": "Installation was complicated and nothing worked correctly.",
        "expected": "negative"
    },
    {
        "review": "The software is full of bugs and keeps crashing.",
        "expected": "negative"
    },
    {
        "review": "I am extremely disappointed with the overall performance.",
        "expected": "negative"
    },
    {
        "review": "I would not recommend this product to anyone.",
        "expected": "negative"
    }
]


correct_predictions = 0

print("\nSmartReview Sentiment Accuracy Evaluation")
print("=" * 50)

for index, sample in enumerate(evaluation_dataset, start=1):
    result = analyze_sentiment(sample["review"])

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
print(f"Total samples:         {total_samples}")
print(f"Correct predictions:   {correct_predictions}")
print(f"Incorrect predictions: {total_samples - correct_predictions}")
print(f"Accuracy:              {accuracy:.2f}%")