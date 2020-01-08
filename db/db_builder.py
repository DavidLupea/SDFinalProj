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

    c.execute("""
    CREATE TABLE IF NOT EXISTS user_profile(
    project TEXT PRIMARY KEY,
    reddit_posts INT,
    address TEXT
    );""")
    c.close()

def create_projects(owner, projectname):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    projectname = owner + "_" + projectname
    c.execute("""
    CREATE TABLE IF NOT EXISTS {}(
    member TEXT PRIMARY KEY,
    task_name TEXT,
    task_desc TEXT,
    task_assigned TEXT,
    task_status TEXT,
    task_due_date TEXT,
    meeting_desc TEXT,
    meeting_location TEXT,
    meeting_date TEXT
    );""")
    c.close()
