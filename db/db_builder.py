import sqlite3

def create_tables():
    db = sqlite3.connect("database.db")
    c = db.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT,
    full_name TEXT
    );""")
    c.close()
