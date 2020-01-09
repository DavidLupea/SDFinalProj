import sqlite3

def add_user(username, password, full_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO users VALUES ('{}', '{}', '{}')"
    command = command.format(username, password, full_name)
    c.execute(command)

    db.commit()
    db.close()

def check_registration(username):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    return len(list(c.execute("SELECT * FROM users WHERE username = '{}'".format(username))))
    db.close()

def is_valid_login(username, password, full_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    return len(list(c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}' AND full_name = '{}';".format(username, password, full_name))))
    db.close()

def add_member(project, member):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    print(project)
    print(member)
    command = "INSERT INTO {} VALUES('{}',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);"
    command = command.format(project, member)
    c.execute(command)
    db.commit()
    db.close()
