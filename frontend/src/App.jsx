import { useEffect, useState } from "react";

import ReviewForm from "./components/ReviewForm";
import AnalysisResult from "./components/AnalysisResult";
import BatchReviewForm from "./components/BatchReviewForm";
import BatchResults from "./components/BatchResults";
import StatsCards from "./components/StatsCards";
import ReviewHistory from "./components/ReviewHistory";

import {
  getReviewHistory,
  getReviewStats,
} from "./services/reviewApi";

import "./App.css";

function App() {
  const [mode, setMode] = useState("single");
  const [analysisResult, setAnalysisResult] = useState(null);
  const [batchResults, setBatchResults] = useState([]);
  const [stats, setStats] = useState(null);
  const [history, setHistory] = useState([]);
  const [dashboardError, setDashboardError] = useState("");

  const refreshDashboard = async () => {
    try {
      setDashboardError("");

      const [statsData, historyData] = await Promise.all([
        getReviewStats(),
        getReviewHistory(10),
      ]);

      setStats(statsData);
      setHistory(historyData);
    } catch {
      setDashboardError("Failed to load review statistics and history.");
    }
  };

  useEffect(() => {
    refreshDashboard();
  }, []);

  const handleAnalysisComplete = async (result) => {
    setAnalysisResult(result);
    await refreshDashboard();
  };

  const handleBatchComplete = async (results) => {
    setBatchResults(results);
    await refreshDashboard();
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <div>
            <h1>SmartReview</h1>
            <p>AI-powered product review intelligence</p>
          </div>

          <span className="status-badge">
            <span className="status-dot"></span>
            System Online
          </span>
        </div>
      </header>

      <main className="app-main">
        <section className="hero">
          <span className="hero-label">REVIEW INTELLIGENCE</span>

          <h2>Understand customer feedback instantly.</h2>

          <p>
            Analyse sentiment, identify suspicious reviews, and discover product
            topics from customer feedback.
          </p>
        </section>

        <div className="mode-switcher">
          <button
            className={`mode-button ${mode === "single" ? "active" : ""}`}
            onClick={() => setMode("single")}
          >
            Single Review
          </button>

          <button
            className={`mode-button ${mode === "batch" ? "active" : ""}`}
            onClick={() => setMode("batch")}
          >
            Batch Analysis
          </button>

          <button
            className={`mode-button ${mode === "statistics" ? "active" : ""}`}
            onClick={() => setMode("statistics")}
          >
            Statistics
          </button>
        </div>

        {mode === "single" && (
          <div className="analysis-grid">
            <ReviewForm onAnalysisComplete={handleAnalysisComplete} />

            <AnalysisResult result={analysisResult} />
          </div>
        )}

        {mode === "batch" && (
          <div className="batch-mode">
            <BatchReviewForm onBatchComplete={handleBatchComplete} />

            <BatchResults results={batchResults} />
          </div>
        )}

        {mode === "statistics" && (
          <div className="statistics-mode">
            {dashboardError && (
              <p className="error-message">{dashboardError}</p>
            )}

            <StatsCards stats={stats} />

            <ReviewHistory reviews={history} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;