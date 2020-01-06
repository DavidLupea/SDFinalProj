from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)

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
	return render_template("main.html")

@app.route("/logout")
def logout():
	return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
