from flask import Flask, render_template, request, session
from flask_session import  Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


notes = []
@app.route("/")     #斜杠指的是默认url
def index():
    headline = "myheadline"
    names = ['David', 'Bob']
    return render_template("index.html", names = names)

# @app.route("/<string:name>")
# def hello(name):
#     return f"<h1>hello {name}</h1>"

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/extendTest")
def extendTest():
    return render_template("extendTest.html")

@app.route("/extendTest2")
def extendTest2():
    return render_template("extendTest2.html")

@app.route("/postTest")
def postTest():
    return render_template("postTest.html")

@app.route("/postTestAnswer", methods=["POST"])  #这里的method意味着这个网站只能通过post的方式访问到，方括号里可以有多个访问方式
def postTestAnswer():
    personName = request.form.get("personName")
    return render_template("postTestAnswer.html", name=personName)

@app.route("/noteTest", methods=["GET", "POST"])
def noteTest():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("noteTest.html", notes=notes)


app.run(debug = True)