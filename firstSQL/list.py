import os
from sqlalchemy import text

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/lecture3")
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute(text('SELECT origin, destination, duration FROM flights')).fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} during {flight.duration} minutes")


if __name__ == "__main__":
    main()