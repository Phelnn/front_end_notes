from flask import Flask, jsonify, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts", methods=["POST"])
def posts():

    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start+9))

    data = []
    for i in range(start, end + 1):
        data.append(f"友友们这家位于解放西{i}号的宝藏小店真是爱了爱了！！！！")

    time.sleep(1)

    return jsonify(data) 


if __name__ == '__main__':
    app.run(debug=True)