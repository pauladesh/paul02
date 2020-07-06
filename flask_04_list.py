from flask import Flask, render_template, redirect, url_for
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("flask_04.html",content = ['Tim','Shilpi', 'Paul'])

if __name__=='__main__':
    app.run(debug=True)
