from flask import Flask, session, render_template, request, redirect, url_for
from db import db_utils, db_builder

app = Flask(__name__)

db_builder.create_tables()

@app.route("/")
def root():
	return render_template("login.html")

@app.route("/auth")
def auth():
	return render_template("main.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/auth_register")
def auth_register():
	if db_utils.check_registration(request.args["username"]) == 0:
		db_utils.add_user(request.args["username"], request.args["full_name"], request.args["password"] )
		return render_template("main.html")
	return render_template("register.html")   ### ADD FLASH ERROR

@app.route("/logout")
def logout():
	return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
