from flask import Flask, render_template, request, session
from flask_session import Session

import os
from sqlalchemy import text

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/lecture3") #原码使用的os.get_url不知道什么原因会报错
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute(text('SELECT * FROM flights')).fetchall()
    return render_template("index.html", flights = flights)

@app.route("/book", methods=["POST"])  
def book():

    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number")
    
    if db.execute(text("SELECT * FROM flights WHERE id = :id"), {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flights")
    db.execute(text("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)"), {"name": name, "flight_id": flight_id}) #和网课原码不同，这里需要给执行的mysql语句加上text()
    db.commit()
    newPassengers = db.execute( text("SELECT * FROM passengers WHERE flight_id = :id"), {"id":flight_id}).fetchall()
    return render_template("success.html", message="SUCCESS")

@app.route("/flights")
def flights():
    flightList = db.execute( text("SELECT * FROM flights")).fetchall()
    return render_template("flights.html", flightList=flightList)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    passengers = db.execute( text("SELECT * FROM passengers WHERE flight_id = :id"), {"id": flight_id}).fetchall()
    cur_flight = db.execute( text("SELECT * FROM flights WHERE id = :id"), {"id":flight_id}).fetchone()
    return render_template("flight.html", passengers=passengers, cur_flight=cur_flight)

if __name__ == '__main__':              #这里的__name__是每一个.py文件都有的内置全局变量，如果这个.py文件被导入时就是__文件名__，如果这个文件直接运行时
    app.run(debug = True)               #默认__name__ = __main__