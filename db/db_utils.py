import sqlite3

def replace_spaces(data):
	return data.replace(" ", "-")

def replace_dashes(data):
	return data.replace("-", " ")

def add_user(username, password, full_name):
	username = replace_spaces(username)
	password = replace_spaces(password)
	full_name = replace_spaces(full_name)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO users VALUES ('{}', '{}', '{}', 100)"
    command = command.format(username, password, full_name)
    c.execute(command)

    db.commit()
    db.close()

def check_registration(username):
	username = replace_spaces(username)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    return len(list(c.execute("SELECT * FROM users WHERE username = '{}'".format(username))))
    db.close()

def is_valid_login(username, password):
	username = replace_spaces(username)
	password = replace_spaces(password)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    return len(list(c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}';".format(username, password))))
    db.close()

def add_member(project, member):
	project = replace_spaces(project)
	member = replace_spaces(member)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES('{}',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);"
    command = command.format(project, member)
    c.execute(command)
    db.commit()
    db.close()

def add_project(username, project_name):
	username = replace_spaces(username)
	project_name = replace_spaces(project_name)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES('{}', NULL);"
    command = command.format(username, project_name)
    c.execute(command)
    db.commit()
    db.close()

def get_projects(username):
	username = replace_spaces(username)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    all_projects = []
    command = "SELECT project FROM {};".format(username)
    for project in list(db.execute(command)):
        project[0] = remove_dashes(project[0])
        all_projects.append(str(project[0]))
    return all_projects
    db.commit()
    db.close()

def add_task(username, project_name, task_name, task_desc, due_date, crystalz):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    # check that the task does not already exist
    command = "INSERT INTO {} VALUES(NULL ,'{}','{}','{}','{}','{}', {},NULL,NULL,NULL);"
    command = command.format(project_name, task_name, task_desc, username, "Incomplete", due_date, crystalz)
    c.execute(command)
    db.commit()
    db.close()

def get_task(project_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "SELECT task_name, task_desc, task_assigned, task_status, task_due_date, task_worth FROM {}".format(project_name)
    tasks = list(c.execute(command))
    db.close()
    return tasks

def add_meeting(project_name, meeting_desc, meeting_location, meeting_date):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES(NULL,NULL,NULL,NULL,NULL,NULL,NULL,'{}','{}','{}');"
    command = command.format(project_name, meeting_desc, meeting_location, meeting_date)
    c.execute(command)
    db.commit()
    db.close()

def complete_task(project_name, task_name, crystalz, username):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "UPDATE {} SET task_status = 'Complete' WHERE task_name ='{}';"
    command = command.format(project_name, task_name)
    user_crystalz = "SELECT crystalz FROM users WHERE username = '{}';"
    user_crystalz = user_crystalz.format(username)
    total_crystalz = int(crystalz) + int(list(c.execute(user_crystalz))[0][0])
    command2 = "UPDATE users SET crystalz = {} WHERE username = '{}';"
    command2 = command2.format(total_crystalz, username)
    c.execute(command)
    c.execute(command2)
    db.commit()
    db.close()

def get_crystalz(username):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "SELECT crystalz FROM users WHERE username = '{}';".format(username)
    crystalz = list(c.execute(command))
    db.commit()
    db.close()
    return crystalz[0][0]
