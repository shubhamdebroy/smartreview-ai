function StatsCards({ stats }) {
  if (!stats) {
    return null;
  }

  const cards = [
    {
      label: "Total Reviews",
      value: stats.total_reviews,
      type: "total",
    },
    {
      label: "Positive",
      value: stats.positive_reviews,
      type: "positive",
    },
    {
      label: "Negative",
      value: stats.negative_reviews,
      type: "negative",
    },
    {
      label: "Neutral",
      value: stats.neutral_reviews,
      type: "neutral",
    },
    {
      label: "Fake Reviews",
      value: stats.fake_reviews,
      type: "fake",
    },
  ];

  return (
    <section className="stats-section">
      <div className="section-heading">
        <div>
          <span className="section-label">OVERVIEW</span>
          <h2>Review Statistics</h2>
        </div>
      </div>

      <div className="stats-grid">
        {cards.map((card) => (
          <article className={`stat-card ${card.type}`} key={card.label}>
            <span>{card.label}</span>
            <strong>{card.value}</strong>
          </article>
        ))}
      </div>
    </section>
  );
}

export default StatsCards;