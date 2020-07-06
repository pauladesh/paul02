from flask import Flask, render_template, redirect, url_for
app=Flask(__name__)

@app.route("/<name>")
def index(name):
    return render_template("helloworld.html", heading=name, para=572039457)

if __name__=="__main__":
    app.run()
