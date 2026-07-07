# SmartReview – AI Product Review Analyzer

SmartReview is a full-stack AI-powered product review analysis application that analyzes customer reviews using sentiment analysis, heuristic fake-review detection, and keyword-based topic extraction.

The application provides single-review analysis, batch processing, review history, and an interactive statistics dashboard through a React frontend connected to a FastAPI backend.

## Features

- AI-based sentiment analysis
- Positive, negative, and neutral sentiment classification
- Sentiment confidence score
- Rule-based suspicious fake-review detection
- Explainable fake-review detection flags
- Suspicion score calculation
- Keyword-based topic extraction
- Single-review analysis
- Batch analysis of up to 50 reviews
- Persistent review history using SQLite
- Review statistics dashboard
- Automatic statistics and history refresh
- Loading and error states
- Responsive frontend interface
- Server-side application logging
- Input and boundary validation
- Reproducible sentiment accuracy evaluation

## Architecture

SmartReview follows a layered application architecture.

```text
React + Vite Frontend
        |
        v
FastAPI Application
        |
        v
Router Layer
        |
        v
Service Layer
        |
        +-------------------------+
        |            |            |
        v            v            v
Sentiment       Fake Review     Topic
Analyzer        Detector        Extractor
        |            |            |
        +------------+------------+
                     |
                     v
               Service Layer
                     |
                     v
              Repository Layer
                     |
                     v
               SQLite Database
```

### Layer Responsibilities

**Router Layer**

Handles HTTP requests and responses, invokes the service layer, and translates internal application failures into controlled HTTP errors.

**Service Layer**

Coordinates the complete review-analysis workflow. It invokes sentiment analysis, fake-review detection, topic extraction, and repository operations.

**Repository Layer**

Handles SQLite database operations and keeps persistence logic separate from business logic.

**Utility Analysis Components**

Contain the sentiment analyzer, heuristic fake-review detector, and keyword-based topic extractor.

This separation improves maintainability and keeps HTTP, business, analysis, and persistence responsibilities independent.

## Project Structure

```text
SmartReview – AI Product Review Analyzer/
|
├── app/
│   ├── database/
│   │   └── database.py
│   ├── repositories/
│   │   └── review_repository.py
│   ├── routers/
│   │   └── review.py
│   ├── schemas/
│   │   └── review_schema.py
│   ├── services/
│   │   └── review_services.py
│   ├── utils/
│   │   ├── fake_review_detector.py
│   │   ├── sentiment_analyzer.py
│   │   └── topic_extractor.py
│   └── main.py
|
├── evaluation/
│   └── evaluate_sentiment.py
|
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AnalysisResult.jsx
│   │   │   ├── BatchResults.jsx
│   │   │   ├── BatchReviewForm.jsx
│   │   │   ├── ReviewForm.jsx
│   │   │   ├── ReviewHistory.jsx
│   │   │   └── StatsCards.jsx
│   │   ├── services/
│   │   │   └── reviewApi.js
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── package-lock.json
|
├── requirements.txt
├── .gitignore
└── README.md
```

## Tech Stack

### Backend

- Python
- FastAPI
- Pydantic
- Hugging Face Transformers
- PyTorch
- SQLite
- Uvicorn

### Frontend

- React
- Vite
- JavaScript
- CSS

### AI Model

- `cardiffnlp/twitter-roberta-base-sentiment-latest`

## Setup Instructions

### Prerequisites

Install:

- Python
- Node.js
- npm

Clone the repository and open the project directory.

## Backend Setup

Create a Python virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux or macOS

```bash
python -m venv venv
source venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI backend:

```bash
uvicorn app.main:app --reload
```

The backend runs locally on:

```text
http://127.0.0.1:8000
```

Swagger API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

The SQLite database and required review table are initialized during application startup.

## Frontend Setup

Open a second terminal and move into the frontend directory:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend normally runs locally on:

```text
http://localhost:5173
```

The FastAPI backend currently allows the local Vite development origin through CORS.

## API Endpoints

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| GET    | `/`                | API welcome endpoint           |
| GET    | `/health`          | Application health check       |
| POST   | `/reviews/analyse` | Analyze a single review        |
| POST   | `/reviews/batch`   | Analyze a batch of reviews     |
| GET    | `/reviews/history` | Retrieve recent review history |
| GET    | `/reviews/stats`   | Retrieve review statistics     |

## Example Analysis Behaviour

Example request:

```json
{
  "review": "The battery life is excellent and the phone performs smoothly."
}
```

The analysis response contains:

```json
{
  "topics": ["battery", "performance"],
  "sentiment": "positive",
  "confidence": 0.9755129814147949,
  "is_fake": false,
  "suspicion_score": 0,
  "flags": []
}
```

The confidence value shown above is only an example of the response structure. The actual confidence score is generated by the sentiment model during inference.

## Sentiment Analysis

SmartReview uses:

```text
cardiffnlp/twitter-roberta-base-sentiment-latest
```

The Transformer model classifies review sentiment into one of three labels:

- positive
- negative
- neutral

The model is loaded once when the sentiment analyzer module is initialized instead of being recreated for every request.

This avoids repeated model-loading overhead during individual review analysis.

SmartReview performs single-label sentiment classification over the model input.

It does not perform Aspect-Based Sentiment Analysis.

Therefore, a mixed review such as:

```text
The display is excellent but the battery life is terrible.
```

receives one overall sentiment classification.

SmartReview does not separately classify:

```text
display -> positive
battery -> negative
```

Inputs exceeding the supported sentiment sequence length are truncated to a maximum of 512 tokens during tokenization before model inference.

Therefore, sentiment analysis of extremely long reviews may not include content beyond the truncated model input.

## Fake-Review Detection

SmartReview uses an explainable rule-based heuristic detector.

It does not use a machine-learning fake-review classification model.

The detector checks four suspicious patterns:

1. Excessive exclamation marks
2. Excessive uppercase letters
3. Suspicious promotional phrases
4. Consecutive repeated words

Examples of suspicious patterns include highly promotional wording, repeated words, excessive capitalization, and excessive exclamation marks.

### Suspicion Score

The suspicion score is calculated as:

```text
Triggered Rules
---------------
 Total Rules
```

The detector currently contains four rules.

For example:

```text
1 triggered rule / 4 rules = 0.25
```

A review is classified as suspicious or fake when:

```text
suspicion_score >= 0.5
```

Therefore:

```text
0.25 -> not fake
0.50 -> fake
0.75 -> fake
1.00 -> fake
```

The response also contains detection flags describing which heuristic rules were triggered.

The detector is intended as an explainable suspicious-pattern detector and should not be interpreted as a definitive authenticity verification system.

## Topic Extraction

SmartReview uses keyword-based topic extraction.

Supported topics are:

- battery
- delivery
- price
- quality
- performance
- support

The topic extractor searches review text for configured topic keywords and returns matching topic categories.

For example:

```text
The battery lasts all day and the phone performs smoothly.
```

may produce:

```json
["battery", "performance"]
```

Topic extraction is not Transformer-based and does not perform semantic topic modeling.

Because extraction uses keyword matching, contextual false positives are possible.

A keyword may appear in a sentence where the broader context does not actually represent the intended product topic.

## Batch Analysis

SmartReview supports batch analysis of between 1 and 50 reviews per request.

The batch workflow reuses the same single-review analysis pipeline.

```text
Batch Request
     |
     v
Review 1 -> analyse_review()
Review 2 -> analyse_review()
Review 3 -> analyse_review()
     |
     v
Combined Response List
```

This avoids duplicating sentiment, fake-review, topic-extraction, and persistence logic.

Batch reviews are currently processed sequentially.

This design is appropriate for the current internship-scale application but may become a performance bottleneck for larger workloads because Transformer inference is performed for each review one after another.

## Statistics Dashboard

The frontend provides statistics for:

- Total analyzed reviews
- Positive reviews
- Negative reviews
- Neutral reviews
- Suspicious fake reviews

Statistics are calculated from persisted SQLite review records.

The dashboard also displays recent review history.

Statistics and history are requested independently using `Promise.all`, allowing both API requests to begin without unnecessarily waiting for one request to finish before starting the other.

After successful analysis, the frontend refreshes statistics and review history to reflect the latest persisted data.

## Persistence

SmartReview uses SQLite for local persistence.

Some Python values require conversion before storage.

Boolean values are stored using SQLite integers:

```text
Python bool
    |
    v
int()
    |
    v
SQLite INTEGER
```

When records are retrieved:

```text
SQLite INTEGER
    |
    v
bool()
    |
    v
Python bool
```

Lists such as topics and fake-review flags are serialized using JSON:

```text
Python list[str]
    |
    v
json.dumps()
    |
    v
SQLite TEXT
```

During retrieval:

```text
SQLite JSON TEXT
    |
    v
json.loads()
    |
    v
Python list[str]
```

Parameterized SQL queries are used instead of constructing SQL statements directly from user input.

## Application Logging

SmartReview uses Python's standard `logging` module for basic server-side application logging.

The application records useful runtime events such as:

- Application startup
- Database initialization
- Successful review analysis
- Successful batch analysis
- Review analysis failures
- Batch analysis failures
- History retrieval failures
- Statistics retrieval failures

The application does not intentionally log complete review content.

Successful operations are recorded using INFO-level logs.

Failures at the HTTP boundary are recorded with exception tracebacks to support debugging while API clients receive controlled error messages.

## Sentiment Accuracy Evaluation

The current Cardiff NLP sentiment analyzer was evaluated using a manually labeled sample dataset containing 30 product-review samples.

The dataset was balanced across the three supported sentiment classes:

```text
10 positive reviews
10 negative reviews
10 neutral reviews
```

Expected sentiment labels were defined in the evaluation dataset and compared with predictions generated by the same `analyse_sentiment()` function used by the SmartReview application.

Accuracy was calculated using:

```text
accuracy = correct predictions / total samples * 100
```

Measured result:

```text
Total samples:         30
Correct predictions:   30
Incorrect predictions: 0
Accuracy:              100.00%
```

The sentiment analyzer therefore achieved 100.00% accuracy on this manually labeled balanced 30-sample evaluation dataset.

This result does not mean that the model is universally 100% accurate.

The evaluation dataset primarily contains clear positive, negative, and neutral product-review statements. More difficult language patterns such as sarcasm, implicit sentiment, highly ambiguous reviews, and complex mixed sentiment may produce different results.

The evaluation can be reproduced using:

```bash
python -m evaluation.evaluate_sentiment
```

## Input Validation

SmartReview validates review requests before analysis.

Empty and whitespace-only reviews are rejected.

Batch requests must contain between 1 and 50 reviews.

Batch items containing empty or whitespace-only reviews are rejected.

Review history limits must remain between 1 and 100.

Invalid schema or query input is rejected through FastAPI and Pydantic validation before reaching the analysis service.

## Known Limitations

- SmartReview does not perform Aspect-Based Sentiment Analysis.
- Sentiment analysis produces one overall sentiment label for each model input.
- Extremely long sentiment inputs are truncated to a maximum of 512 tokens before inference.
- Content beyond the truncated model input may not influence the sentiment prediction.
- Fake-review detection is heuristic-based and is not an ML-based authenticity classifier.
- Heuristic fake-review detection can produce false positives or false negatives.
- Topic extraction is keyword-based.
- Topic extraction is not Transformer-based or semantic topic modeling.
- Keyword topic matching can produce contextual false positives.
- Batch analysis is processed sequentially.
- Transformer sentiment inference is the primary processing bottleneck.
- SQLite is appropriate for the current project scale but is not intended for large distributed workloads.
- The current application is designed as a single-server internship-scale system.

The final local demo dataset was recreated after changing the sentiment model and generated only through the current Cardiff NLP sentiment analysis pipeline. Historical rows generated by the previous DistilBERT SST-2 model were removed from the development database before the final demo dataset was created.

## Future Improvements

Possible future improvements include:

- Aspect-Based Sentiment Analysis for per-topic sentiment
- ML-based fake-review classification using a labeled authenticity dataset
- Semantic or Transformer-based topic extraction
- Improved evaluation using a larger external labeled review dataset
- Parallel or asynchronous batch-processing strategies
- Background job processing for large review batches
- PostgreSQL or another production-oriented database
- Caching repeated analysis requests
- Model-serving optimization
- Horizontal application scaling
- Load balancing across multiple application instances
- Queue-based processing for large workloads
- Authentication and user-specific review history
- Production deployment and monitoring

These improvements are intentionally outside the scope of the current internship project.

## Final Project Scope

SmartReview demonstrates the integration of:

- Transformer-based sentiment analysis
- Explainable heuristic analysis
- Keyword-based text processing
- FastAPI backend development
- Layered backend architecture
- Pydantic request and response validation
- SQLite persistence
- React frontend development
- Frontend and backend API integration
- Batch processing
- Statistics aggregation
- Application logging
- Model evaluation
- Edge-case and API validation

The project focuses on a maintainable and explainable internship-scale architecture without introducing unnecessary distributed-system complexity.
