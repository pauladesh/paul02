from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>Namaste India</h1>"

@app.route("/paul")
def Paul():
    return "Hey Paul!"
