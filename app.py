from flask import Flask, session, render_template, request, redirect, url_for
from db import db_utils, db_builder
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
db_builder.create_tables()

@app.route("/")
def root():
    if "username" in session:
        return render_template("main.html")
    else:
        return redirect(url_for("login"))

@app.route("/login")
def login():
	print(len(request.args))
	if len(request.args) == 3:
	    # User entered login information
		username = request.args["username"]
		password = request.args["password"]
		full_name = request.args["full_name"]
		if db_utils.is_valid_login(username, password, full_name):
			session["username"] = username
			print("Logged into account with username: " + username)
			return render_template("main.html")
		else:
			print("Wrong username or password")

	return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/auth_register")
def auth_register():
	if db_utils.check_registration(request.args["username"]) == 0:
		db_utils.add_user(request.args["username"], request.args["password"], request.args["full_name"] )
		return render_template("main.html")
	return render_template("register.html")   ### ADD FLASH ERROR

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    # app.secret_key()
    app.run()
