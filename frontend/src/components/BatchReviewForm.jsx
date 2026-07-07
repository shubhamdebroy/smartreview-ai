import { useState } from "react";
import { analyseBatch } from "../services/reviewApi";

function BatchReviewForm({ onBatchComplete }) {
  const [batchInput, setBatchInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    const reviews = batchInput
      .split("\n")
      .map((review) => review.trim())
      .filter((review) => review.length > 0);

    if (reviews.length === 0) {
      setError("Please enter at least one review.");
      return;
    }

    if (reviews.length > 50) {
      setError("A maximum of 50 reviews can be analysed at once.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const results = await analyseBatch(reviews);

      onBatchComplete(results);
      setBatchInput("");
    } catch {
      setError("Failed to analyse batch reviews.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card batch-card">
      <div className="card-header">
        <div>
          <h3>Batch Analysis</h3>
          <p>Analyse multiple customer reviews in one request.</p>
        </div>
      </div>

      <form className="review-form" onSubmit={handleSubmit}>
        <label htmlFor="batch-reviews">Customer reviews</label>

        <textarea
          id="batch-reviews"
          value={batchInput}
          onChange={(event) => setBatchInput(event.target.value)}
          placeholder={`Enter one review per line...\n\nThe battery life is excellent.\nDelivery was very slow.\nVERY GOOD!!! BUY NOW!!!`}
          rows="10"
        />

        <span className="input-hint">
          One review per line · Maximum 50 reviews
        </span>

        {error && <p className="error-message">{error}</p>}

        <button className="primary-button" type="submit" disabled={loading}>
          {loading ? "Analysing batch..." : "Analyse Batch"}
        </button>
      </form>
    </section>
  );
}

export default BatchReviewForm;
