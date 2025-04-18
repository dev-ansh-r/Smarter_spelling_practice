# scripts/seed_dictionary.py
import sqlite3
import requests

DB_PATH = "data/user_db.sqlite"
WORDLIST_URL = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"

def download_wordlist(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def seed_database(words):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS dictionary (word TEXT PRIMARY KEY)')
    for word in words:
        try:
            c.execute('INSERT OR IGNORE INTO dictionary (word) VALUES (?)', (word.strip().lower(),))
        except Exception as e:
            print(f"Failed to insert {word}: {e}")
    conn.commit()
    conn.close()
    print(f"[✅] Seeded {len(words)} words into the dictionary.")

if __name__ == '__main__':
    print("[⬇️] Downloading word list...")
    words = download_wordlist(WORDLIST_URL)
    print("[💾] Seeding into SQLite...")
    seed_database(words)
