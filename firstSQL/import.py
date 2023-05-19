import csv
import os
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/lecture3")
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute(text('INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)'), {"origin":origin, "destination": destination, "duration": duration} )  #逗号前使用字典告诉占位符中填什么， 冒号加变量用于给还未确定的数据占位
        print(f"Added flight from {origin} to {destination} lasting {duration}")
    db.commit()


if __name__ == "__main__":
    main()