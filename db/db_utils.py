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
    command = "INSERT INTO users VALUES ('{}', '{}', '{}')"
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

def is_valid_login(username, password, full_name):
	username = replace_spaces(username)
	password = replace_spaces(password)
	full_name = replace_spaces(full_name)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    return len(list(c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}' AND full_name = '{}';".format(username, password, full_name))))
    db.close()

def add_member(project, member):
	project = replace_spaces(project)
	member = replace_spaces(member)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES('{}',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);"
    command = command.format(project, member)
    c.execute(command)
    db.commit()
    db.close()

def add_project(username, project_name):
	username = replace_spaces(username)
	project_name = replace_spaces(project_name)
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES('{}', 0, NULL);"
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

# HERE

def add_task(username, project_name, task_name, task_desc, due_date):
	
    db = sqlite3.connect("database.db")
    c = db.cursor()
    # check that the task does not already exist
    command = "INSERT INTO {} VALUES(NULL ,'{}','{}','{}','{}','{}',NULL,NULL,NULL);"
    command = command.format(project_name, task_name, task_desc, username, "Incomplete", due_date)
    c.execute(command)
    db.commit()
    db.close()

def get_task(project_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "SELECT task_name, task_desc, task_status, task_assigned, task_due_date FROM {}".format(project_name)
    tasks = list(c.execute(command))
    db.close()
    return tasks

def add_meeting(project_name, meeting_desc, meeting_location, meeting_date):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "INSERT INTO {} VALUES(NULL,NULL,NULL,NULL,NULL,NULL,'{}','{}','{}');"
    command = command.format(project_name, meeting_desc, meeting_location, meeting_date)
    c.execute(command)
    db.commit()
    db.close()

def complete_task(project_name, task_name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    command = "UPDATE {} SET task_status = 'Complete' WHERE task_name ='{}'"
    command = command.format(project_name, task_name)
    print(command)
    c.execute(command)
    db.commit()
    db.close()
