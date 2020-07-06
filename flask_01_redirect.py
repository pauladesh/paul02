from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route("/")
def home():
    return "Hi, welcome to my page"

@app.route("/<name>")
def user(name):
    return f"Hi {name}"

@app.route("/admin")
def admin():
    return redirect (url_for("user",name='Adesh'))

if __name__=="__main__":
    app.run()
