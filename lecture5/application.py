# Socket.IO
import requests
import os
import gevent
import geventwebsocket
import logging
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app._static_folder = "./templates/static"

# if not app.debug:
#     # 非调试模式下启用日志记录
#     print('here')
#     log_handler = logging.FileHandler('flask.log')
#     log_handler.setLevel(logging.WARNING)
#     app.logger.addHandler(log_handler)       

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")     #这个函数开启对客户端信息的监听，"submit vote"是自定义事件，对应客户端（即index.js文件）中socket.emit('submit vote')
def vote(data):
    selection = data["selection"]
    emit("annouce vote", {"selection": selection}, broadcast = True)


if __name__ == '__main__':              #这里的__name__是每一个.py文件都有的内置全局变量，如果这个.py文件被导入时就是__文件名__，如果这个文件直接运行时默认__name__ = __main__
    socketio.run(app,  debug=True)  
      
