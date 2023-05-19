from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(64), nullable=False)
    destination = db.Column(db.String(64), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Pssenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable="False")

