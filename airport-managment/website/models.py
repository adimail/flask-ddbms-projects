from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    is_pilot = db.Column(db.Boolean, nullable=False, default=False)

    flights = relationship('Flight', backref='user', lazy=True)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gate = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    aircraft = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    pilot_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
