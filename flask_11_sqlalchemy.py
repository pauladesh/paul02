from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='dsfg3726892^*^UGjgut6&%I^jgh'
app.config['SQLAlchemy_DATABASE_URI']='sqlite:///users.sqlite3'  #'sqlite:///<table name>.sqlite3' setting up configuration properties for an app to define some stuff to do with the database.
app.config["SQLAlchemy_TRACK_MODIFICATIONS"]=False #It's used to close warnings
app.permanent_session_lifetime = timedelta(minutes=5)

db= SQLAlchemy(app) #setting up database object

class users(db.Model): #defining a class whoch represents the user object in database
    _id=db.Column("id", db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(150))

    def __init__(self, name, email): #this method takes variables that we need to create new objects
        self.name=name
        self.email=email


@app.route("/")
def home():
        return render_template("flask_07_home.html")

@app.route("/view")
def view():
        return render_template("flask_11_view.html", values=users.query.all())


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form['nm']
        session['user']=user

        found_user = users.query.filter_by(name=user).first()  #when we view our data or find our data, it gets the data (filter_by) by FCFS
        if found_user:
            session['email']=found_user.email

        else:                       # If the user does not exist, we add a new one to database
            usr=users(user, "")
            db.session.add(usr)     #adding the user model to our database
            db.session.commit()     #Everytime you make change to your database, you need to commit it.

        flash("Login Successfully!")
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            flash('already logged in')
            return redirect(url_for("user"))

        return render_template("flask_10_login.html")


@app.route("/user", methods=["POST","GET"])
def user():
    email=None
    if "user" in session:
        user=session['user']

        if request.method=="POST":
            email= request.form["email"]
            session["email"]=email
            found_user = users.query.filter_by(name=user).first()
            found_user.email=email
            db.session.commit()
            flash('email is saved successfully.')
        else:
            if 'email' in session:
                email=session["email"]

        return render_template("flask_11_user.html", email=email)
    else:
        flash("You\'re not logged logged in.")
        return render_template("flask_10_login.html")





@app.route("/logout")
def logout():
    flash ("You have been logged out", 'info')
    session.pop("user", None)
    session.pop("email", None)
    return render_template("flask_10_login.html")


if __name__=='__main__':
    db.create_all() #create this database if it does not exist in our  program whenever we run this app
    app.run(debug=True)
