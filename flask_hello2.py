from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    headline_py_var="hello"
    return render_template("hello2.html",headline_html_var=headline_py_var)

@app.route("/paul")
def new():
    headline_py_var="hello paul"
    return render_template("hello2.html",headline_html_var=headline_py_var)
