from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("flask_05_child.html", content='You\'re so good.')

if __name__=="__main__":
    app.run(debug=True)
