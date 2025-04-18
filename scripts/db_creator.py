# scripts/create_db.py
import sqlite3

def create_tables():
    conn = sqlite3.connect('data/user_db.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS word_logs (
                 word TEXT PRIMARY KEY,
                 repetitions INTEGER,
                 interval INTEGER,
                 easiness REAL,
                 next_due TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Database tables created successfully.")