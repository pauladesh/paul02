from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("flask_06_child.html", content='You\'re so good.')

@app.route("/test")
def test():
    return render_template("flask_06_new.html")

if __name__=="__main__":
    app.run(debug=True)
