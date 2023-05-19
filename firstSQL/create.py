import os
import mysql
from flask import Flask, render_template, request
from models import *

#原来使用的lecture3数据库，发现程序运行不报错，但是不新建表，其实是lecture3里已经有了同名表，改成使用lecture4后成功建表
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/lecture4"  #原：os.getenv("mysql+pymysql://root:@127.0.0.1:3306/lecture4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()