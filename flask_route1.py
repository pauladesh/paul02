from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>Type your name</h1>"
@app.route("/<string:name>")
def name(name):
    name=name.capitalize()
    return f"Hi, {name}"
