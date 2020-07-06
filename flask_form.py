from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("form_index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return "Please submit your name"
    else:
        name=request.form.get("name")
        return render_template("form_hello.html",name=name)

if __name__=="__main__":
    app.run(debug=True)
    
