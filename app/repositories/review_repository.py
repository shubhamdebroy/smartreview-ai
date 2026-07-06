import json
import sqlite3
from app.database.database import get_db_connection

def save_review(review: str,
                topics: list[str],
                sentiment: str,
                confidence: float,
                is_fake: bool,
                suspicion_score: float,
                flags: list[str]
                ):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO reviews (review, topics, sentiment, confidence, is_fake, suspicion_score, flags)
                       VALUES (?, ?, ?, ?, ?, ?, ?)
                       ''', (review, json.dumps(topics), sentiment, confidence, int(is_fake), suspicion_score, json.dumps(flags)))
        conn.commit()

def get_all_reviews(limit: int):
    with get_db_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM reviews ORDER BY id DESC LIMIT ?',
            (limit,)
        )
        rows = cursor.fetchall()
        reviews = [dict(row) for row in rows]
        for review_data in reviews:
            review_data['topics'] = json.loads(review_data['topics'])
            review_data['is_fake'] = bool(review_data['is_fake'])
            review_data['flags'] = json.loads(review_data['flags'])

    return reviews

def get_review_statistics():
    with get_db_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT COUNT(*) AS total_reviews,
                                SUM(CASE WHEN sentiment = 'positive' THEN 1 ELSE 0 END) AS positive_reviews,
                                SUM(CASE WHEN sentiment = 'negative' THEN 1 ELSE 0 END) AS negative_reviews,
                                SUM(CASE WHEN sentiment = 'neutral' THEN 1 ELSE 0 END) AS neutral_reviews,
                                SUM(CASE WHEN is_fake = 1 THEN 1 ELSE 0 END) AS fake_reviews
                        FROM reviews
                       ''')
        row = cursor.fetchone()
        statistics = dict(row)

    return statistics