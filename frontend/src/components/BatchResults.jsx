function BatchResults({ results }) {
  if (!results || results.length === 0) {
    return null;
  }

  return (
    <section className="batch-results-section">
      <div className="section-heading">
        <div>
          <span className="section-label">BATCH RESULTS</span>
          <h2>Review Analysis</h2>
        </div>

        <span className="result-count">
          {results.length} {results.length === 1 ? "review" : "reviews"}
        </span>
      </div>

      <div className="batch-results-grid">
        {results.map((result, index) => (
          <article
            className={`batch-result-card ${
              result.is_fake ? "fake-review-card" : ""
            }`}
            key={index}
          >
            <div className="batch-result-header">
              <span className="review-number">Review {index + 1}</span>

              <span className={`sentiment-badge ${result.sentiment}`}>
                {result.sentiment}
              </span>
            </div>

            <div className="batch-confidence">
              <span>Confidence</span>
              <strong>{(result.confidence * 100).toFixed(2)}%</strong>
            </div>

            <div className="progress-track">
              <div
                className="progress-value"
                style={{ width: `${result.confidence * 100}%` }}
              ></div>
            </div>

            <div className="batch-detail">
              <span className="result-label">Topics</span>

              <div className="topic-list">
                {result.topics.length > 0 ? (
                  result.topics.map((topic) => (
                    <span className="topic-badge" key={topic}>
                      {topic}
                    </span>
                  ))
                ) : (
                  <span className="result-value">No topics detected</span>
                )}
              </div>
            </div>

            <div className="batch-metrics">
              <div className={result.is_fake ? "fake-status-box" : ""}>
                <span>Fake Review</span>

                <strong
                  className={
                    result.is_fake ? "fake-status detected" : "fake-status safe"
                  }
                >
                  {result.is_fake ? "⚠ Detected" : "Not detected"}
                </strong>
              </div>

              <div>
                <span>Suspicion</span>
                <strong>{(result.suspicion_score * 100).toFixed(2)}%</strong>
              </div>
            </div>

            <div className="batch-detail">
              <span className="result-label">Detection Flags</span>

              {result.flags.length > 0 ? (
                <ul className="flags-list">
                  {result.flags.map((flag, flagIndex) => (
                    <li key={flagIndex}>{flag}</li>
                  ))}
                </ul>
              ) : (
                <p className="no-flags">No suspicious patterns detected.</p>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

export default BatchResults;
