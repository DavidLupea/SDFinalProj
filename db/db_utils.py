import sqlite3

# untested
def add_user(username, password, full_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = 'INSERT INTO users VALUES ({}, {}, {})'
    command = command.format(username, full_name, password)
    c.execute(command)

    db.commit()
    db.close()

def check_registration(username):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    return len(list(c.execute("SELECT * FROM users WHERE username = {}".format(username))))
