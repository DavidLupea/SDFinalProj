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
    command = "INSERT INTO {} VALUES('{}',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);"
    command = command.format(project, member)
    c.execute(command)
    db.commit()
    db.close()

def add_project(username, project_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES('{}', 0, NULL);"
    command = command.format(username, project_name)
    c.execute(command)
    db.commit()
    db.close()

def get_projects(username):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    all_projects = ""
    command = "SELECT project FROM {};".format(username)
    for project in list(db.execute(command)):
        print(project[0])
        all_projects += str(project[0]) + " "
    return all_projects
    db.commit()
    db.close()

def add_task(username, project_name, task_name, task_desc, due_date):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES(NULL ,'{}','{}','{}','{}','{}',NULL,NULL,NULL);"
    command = command.format(project_name, task_name, task_desc, username, "Incomplete", due_date)
    c.execute(command)
    db.commit()
    db.close()
