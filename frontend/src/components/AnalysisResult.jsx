function AnalysisResult({ result }) {
  if (!result) {
    return (
      <section className="card result-card empty-result">
        <div className="empty-result-content">
          <span className="empty-icon">◎</span>

          <h3>Analysis Result</h3>

          <p>
            Submit a product review to view sentiment, confidence, topics, and
            fake review indicators.
          </p>
        </div>
      </section>
    );
  }

  return (
    <section className="card result-card">
      <div className="card-header">
        <div>
          <h3>Analysis Result</h3>
          <p>AI-generated review intelligence.</p>
        </div>

        <span className={`sentiment-badge ${result.sentiment}`}>
          {result.sentiment}
        </span>
      </div>

      <div className="confidence-block">
        <div className="metric-heading">
          <span>Sentiment confidence</span>
          <strong>{(result.confidence * 100).toFixed(2)}%</strong>
        </div>

        <div className="progress-track">
          <div
            className="progress-value"
            style={{ width: `${result.confidence * 100}%` }}
          ></div>
        </div>
      </div>

      <div className="result-grid">
        <div className="result-item">
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

        <div className="result-item">
          <span className="result-label">Fake Review</span>

          <strong className="result-value">
            {result.is_fake ? "Detected" : "Not detected"}
          </strong>
        </div>

        <div className="result-item">
          <span className="result-label">Suspicion Score</span>

          <strong className="result-value">
            {(result.suspicion_score * 100).toFixed(2)}%
          </strong>
        </div>
      </div>

      <div className="flags-section">
        <span className="result-label">Detection Flags</span>

        {result.flags.length > 0 ? (
          <ul className="flags-list">
            {result.flags.map((flag, index) => (
              <li key={index}>{flag}</li>
            ))}
          </ul>
        ) : (
          <p className="no-flags">No suspicious patterns detected.</p>
        )}
      </div>
    </section>
  );
}

export default AnalysisResult;
