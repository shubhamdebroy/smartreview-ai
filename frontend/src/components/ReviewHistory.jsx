function ReviewHistory({ reviews }) {
  return (
    <section className="history-section">
      <div className="section-heading">
        <div>
          <span className="section-label">RECENT ACTIVITY</span>
          <h2>Recent Reviews</h2>
        </div>
      </div>

      {reviews.length === 0 ? (
        <div className="card history-empty">
          <p>No review history available.</p>
        </div>
      ) : (
        <div className="history-list">
          {reviews.map((review) => (
            <article
              className={`history-card ${
                review.is_fake ? "fake-history-card" : ""
              }`}
              key={review.id}
            >
              <div className="history-content">
                <p className="history-review">{review.review}</p>

                <div className="topic-list">
                  {review.topics.map((topic) => (
                    <span className="topic-badge" key={topic}>
                      {topic}
                    </span>
                  ))}
                </div>
              </div>

              <div className="history-metrics">
                <span className={`sentiment-badge ${review.sentiment}`}>
                  {review.sentiment}
                </span>

                <span className={review.is_fake ? "history-fake" : "history-safe"}>
                  {review.is_fake ? "⚠ Fake detected" : "Authentic"}
                </span>

                <span>
                  {(review.confidence * 100).toFixed(2)}% confidence
                </span>
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

export default ReviewHistory;