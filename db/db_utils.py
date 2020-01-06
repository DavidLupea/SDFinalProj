import sqlite3


def add_user(username, password):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()

    command = 'INSERT INTO users VALUES ({}, {}, {}, {})'
    command = command.format(username, password, full_name)
    c.execute(command)

    db.commit()
    db.close()
