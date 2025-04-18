# srs_engine/sm2.py
from datetime import datetime, timedelta
import sqlite3

def update_schedule(word, correct):
    conn = sqlite3.connect('data/user_db.sqlite')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS word_logs (
                 word TEXT PRIMARY KEY,
                 repetitions INTEGER,
                 interval INTEGER,
                 easiness REAL,
                 next_due TEXT)''')

    c.execute('SELECT * FROM word_logs WHERE word=?', (word,))
    row = c.fetchone()

    if row:
        repetitions, interval, easiness = row[1], row[2], row[3]
    else:
        repetitions, interval, easiness = 0, 1, 2.5

    if correct:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval *= easiness
        repetitions += 1
        easiness = max(1.3, easiness + 0.1)
    else:
        repetitions, interval = 0, 1
        easiness = max(1.3, easiness - 0.2)

    next_due = (datetime.now() + timedelta(days=interval)).isoformat()
    c.execute('REPLACE INTO word_logs VALUES (?, ?, ?, ?, ?)',
              (word, repetitions, int(interval), easiness, next_due))
    conn.commit()
    conn.close()
    return {"next_due": next_due, "interval": interval}


def get_due_words():
    now = datetime.now().isoformat()
    conn = sqlite3.connect('data/user_db.sqlite')
    c = conn.cursor()
    c.execute('SELECT word FROM word_logs WHERE next_due <= ?', (now,))
    words = [row[0] for row in c.fetchall()]
    conn.close()
    return words

def is_word_valid(word):
    conn = sqlite3.connect('data/user_db.sqlite')
    c = conn.cursor()
    c.execute('SELECT 1 FROM dictionary WHERE word=?', (word.strip().lower(),))
    result = c.fetchone()
    conn.close()
    return result is not None
