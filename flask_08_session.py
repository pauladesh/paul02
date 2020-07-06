from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta


app=Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("flask_07_home.html")


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form["nm"]
        session["user"]=user #stores user as a dictionary.
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return  redirect(url_for("user"))

        return render_template("flask_07_login.html")


@app.route("/user")
def user():
    if "user" in session:       # to check whether user in session because when user is not in session, so anyone can type /user and enter into his profile.
        user=session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user",None)  #removes user data from session.
    return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True)
