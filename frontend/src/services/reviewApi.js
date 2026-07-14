const API_BASE_URL = "https://smartreview-ai.up.railway.app/";

const request = async (endpoint, options = {}) => {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, options);

  if (!response.ok) {
    throw new Error("API request failed");
  }

  return response.json();
};

export const analyseReview = async (review) => {
  return request("/reviews/analyse", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ review }),
  });
};

export const analyseBatch = async (reviews) => {
  return request("/reviews/batch", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ reviews }),
  });
};

export const getReviewStats = async () => {
  return request("/reviews/stats");
};

export const getReviewHistory = async (limit = 10) => {
  return request(`/reviews/history?limit=${limit}`);
};