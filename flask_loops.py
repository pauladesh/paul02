from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def loops_names():
    names=["Adesh","Adhiraj","Akshay","David"]
    return render_template("loops_names.html", names=names)
