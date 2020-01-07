import sqlite3

# untested
def add_user(username, password):
    db = sqlite3.connect("database.db")
    c = db.cursor()

    command = 'INSERT INTO users VALUES ({}, {}, {}, {})'
    command = command.format(username, password, full_name)
    c.execute(command)

    db.commit()
    db.close()
