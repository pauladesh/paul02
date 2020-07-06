from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app=Flask(__name__)
app.secret_key='hello'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
        return render_template("flask_07_home.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form['nm']
        session['user']=user
        flash("Login Successfully!")
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            flash('already logged in')
            return redirect(url_for("user"))

        return render_template("flask_10_login.html")


@app.route("/user")
def user():
    if "user" in session:
        user=session['user']
        return render_template("flask_10_user.html", user=user)
    else:
        flash("You\'re not logged logged in.")
        return render_template("flask_10_login.html")

@app.route("/logout")
def logout():
    flash ("You have been logged out", 'info')
    session.pop("user", None)
    return render_template("flask_10_login.html")


if __name__=='__main__':
    app.run(debug=True)
