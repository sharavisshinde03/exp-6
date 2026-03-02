from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Sharavi Shinde</h1><br><h2>App ID: 2410915</h2>"

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)