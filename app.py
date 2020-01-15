from flask import Flask, session, render_template, request, redirect, url_for
from db import db_utils, db_builder
import os

app = Flask(__name__)
app.secret_key = "apple pie"
db_builder.create_tables()

@app.route("/")
def root():
    if "username" in session:
        return render_template("main.html")
    else:
        return redirect(url_for("login"))

@app.route("/login")
def login():
    if len(request.args) >= 2:
        # User entered login information
        username = request.args["username"]
        password = request.args["password"]
        if db_utils.is_valid_login(username, password):
            session["username"] = username
            return render_template("main.html")
        else:
            render_template("login.html")
    return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/auth_register")
def auth_register():
    if db_utils.check_registration(request.args["username"]) == 0:
        db_utils.add_user(request.args["username"], request.args["password"], request.args["full_name"] )
        db_builder.create_username(request.args["username"])
        return render_template("login.html")
    return render_template("register.html")   ### ADD FLASH ERROR

@app.route("/create_project")
def create_project():
    return render_template("create_project.html")

@app.route("/process_project")
def process_project():
    db_builder.create_projects(session["username"], request.args["title"])
    members = request.args.to_dict()
    project_name = session["username"] + "_" + request.args["title"]
    i = 1
    while (i < len(request.args)):
        db_utils.add_member(project_name, list(members.values())[i])
        db_utils.add_project(list(members.values())[i], project_name)
        i += i
    return render_template("main.html")

@app.route("/view_projects")
def view_projects():
    project_list = db_utils.get_projects(session["username"])
    return render_template("project_lists.html", project_list = project_list)

@app.route("/actually_view_projects")
def list_projects():
    username = request.args["project"].split("_")[0]
    if session["username"] == username:
        session["project"] = request.args["project"]
        tasks = db_utils.get_task(session["project"])
        meetings = db_utils.get_meeting(session["project"])
        return render_template("project.html", owner = True, task = tasks, meeting = meetings)
    return render_template("project.html", task = tasks)

@app.route("/process_task")
def process_task():
    db_utils.add_task(request.args["username"], session["project"], request.args["task_name"], request.args["task_desc"], request.args["due_date"], request.args["crystalz"])
    tasks = db_utils.get_task(session["project"])
    meetings = db_utils.get_meeting(session["project"])
    return render_template("project.html", owner = True, task = tasks, meeting = meetings)

@app.route("/process_meeting")
def process_meeting():
    db_utils.add_meeting(session["project"], request.args["meeting_desc"], request.args["meeting_location"], request.args["meeting_date"])
    tasks = db_utils.get_task(session["project"])
    meetings = db_utils.get_meeting(session["project"])

    return render_template("project.html", owner = True, task = tasks, meeting = meetings)

@app.route("/complete_task")
def complete_task():
    print("------------------------------------")
    print(request.args["submit"].split("'"))
    print("------------------------------------")
    print(request.args["submit"].split("'")[5])
    
    task_name = request.args["submit"].split("'")[1]
    task_assigned = request.args["submit"].split("'")[5]
    crystalz = request.args["submit"].split("'")[3]
    db_utils.complete_task(session["project"], task_name, crystalz, task_assigned)
    username = session["project"].split("_")[0]
    if session["username"] == username:
        tasks = db_utils.get_task(session["project"])
        meetings = db_utils.get_meeting(session["project"])
        return render_template("project.html", owner = True, task = tasks, meeting = meetings)
    return render_template("project.html", task = tasks)

@app.route("/shop")
def shop():
    crystalz = db_utils.get_crystalz(session["username"])
    return render_template("shop.html", crystalz = crystalz)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("root"))


if __name__ == "__main__":
    app.debug = True
    app.run()
