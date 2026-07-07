import { useState } from "react";
import { analyseReview } from "../services/reviewApi";

function ReviewForm({ onAnalysisComplete }) {
  const [review, setReview] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!review.trim()) {
      setError("Please enter a review.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const result = await analyseReview(review);

      onAnalysisComplete(result);
      setReview("");
    } catch {
      setError("Failed to analyse review.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card review-card">
      <div className="card-header">
        <div>
          <h3>Analyse Review</h3>
          <p>Enter a customer review to generate an AI analysis.</p>
        </div>
      </div>

      <form className="review-form" onSubmit={handleSubmit}>
        <label htmlFor="review">Customer review</label>

        <textarea
          id="review"
          value={review}
          onChange={(event) => setReview(event.target.value)}
          placeholder="Example: The battery life is excellent and the product feels premium..."
          rows="8"
        />

        {error && <p className="error-message">{error}</p>}

        <button className="primary-button" type="submit" disabled={loading}>
          {loading ? "Analysing review..." : "Analyse Review"}
        </button>
      </form>
    </section>
  );
}

export default ReviewForm;
