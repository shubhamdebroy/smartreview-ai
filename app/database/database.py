import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "smartreview.db"

def initialize_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS reviews (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        review TEXT NOT NULL,
                        topics TEXT NOT NULL,
                        sentiment TEXT NOT NULL,
                        confidence REAL NOT NULL,
                        is_fake INTEGER NOT NULL,
                        suspicion_score REAL NOT NULL,
                        flags TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()