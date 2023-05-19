from flask import Flask, render_template

app = Flask(__name__)

texts = ['1111111111111111111111111111111',
         '2222222222222222222222222222222',
         '3333333333333333333333333333333']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]

if __name__ == "__main__":
    app.run(debug=True)