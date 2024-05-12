from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Flight, Booking
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        if current_user.is_pilot:
            gate = request.form.get('gate')
            origin = request.form.get('origin')
            destination = request.form.get('destination')
            aircraft = request.form.get('aircraft')
            duration = request.form.get('duration')

            new_flight = Flight(gate=gate, origin=origin, destination=destination, aircraft=aircraft, duration=duration, pilot_id=current_user.id)
            db.session.add(new_flight)
            db.session.commit()
            flash('Flight added!', category='success')
            return redirect(url_for('views.home'))
        else:
            flight_id = request.form.get('flight_id')
            booking = Booking(user_id=current_user.id, flight_id=flight_id)
            db.session.add(booking)
            db.session.commit()
            flash('Booking confirmed!', category='success')

    if current_user.is_pilot:
        user_flights = Flight.query.filter_by(pilot_id=current_user.id).all()
        allflights = Flight.query.all()
        return render_template("home.html", current_user=current_user, flights=user_flights, allflights=allflights)
    else:
        allflights = Flight.query.all()
        return render_template("home.html", current_user=current_user, allflights=allflights)


@views.route('/delete-flight', methods=['POST'])
@login_required
def delete_flight():
    data = json.loads(request.data) 
    flight_id = data['flight_id']
    flight = Flight.query.get(flight_id)
    if flight:
        if flight.pilot_id == current_user.id:
            db.session.delete(flight)
            db.session.commit()
            flash('Flight removed!', category='danger')

    return jsonify({})

@views.route('/delete-booking', methods=['POST'])
@login_required
def delete_booking():
    data = json.loads(request.data)
    flight_id = data['flight_id']
    booking = Booking.query.filter_by(user_id=current_user.id, flight_id=flight_id).first()
    if booking:
        db.session.delete(booking)
        db.session.commit()
        flash('Booking removed!', category='danger')

    return jsonify({})
