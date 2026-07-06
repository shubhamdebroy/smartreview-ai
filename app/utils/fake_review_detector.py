def detect_fake_review(review: str):

    flags = []
    #rule-1
    if review.count("!") >= 3:
        flags.append("Excessive use of exclamation marks")

    #rule-2
    letters = [char for char in review if char.isalpha()]
    if letters:
        uppercase_count = sum(1 for char in letters if char.isupper())
        uppercase_ratio = uppercase_count / len(letters)
    
        if uppercase_ratio > 0.6:
            flags.append("Excessive use of uppercase letters")
    
    #rule-3 and rule-4
    suspicious_phrases = [
        "best product ever",
        "must buy",
        "life-changing",
        "100% recommended",
        "buy now",
        "limited time offer",
        "guaranteed"
    ]
    if any(phrase in review.lower() for phrase in suspicious_phrases):
        flags.append("Contains suspicious phrases")

    words = review.lower().split()
    for i in range(len(words)-2):
        if words[i] == words[i+1] == words[i+2]:
            flags.append("Contains repeated words")
            break

    total_rules = 4
    suspicion_score = len(flags) / total_rules

    is_fake = suspicion_score >= 0.5

    return {
        "is_fake": is_fake,
        "suspicion_score": suspicion_score,
        "flags": flags
    }