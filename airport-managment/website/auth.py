from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Flight, Booking
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Sign up to create a new account.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def manage():
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
        else:
            flight_id = request.form.get('flight_id')
            booking = Booking(user_id=current_user.id, flight_id=flight_id)
            db.session.add(booking)
            db.session.commit()
            flash('Booking confirmed!', category='success')

    if current_user.is_pilot:
        user_flights = Flight.query.filter_by(pilot_id=current_user.id).all()
        return render_template("profile.html", user=current_user, flights=user_flights)
    else:
        available_flights = Flight.query.all()
        user_bookings = Booking.query.filter_by(user_id=current_user.id).all()
        booked_flights = []
        for booking in user_bookings:
            flight = Flight.query.get(booking.flight_id)
            booked_flights.append(flight)
        return render_template("profile.html", user=current_user, booked_flights=booked_flights, available_flights=available_flights,)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        dob_str = request.form.get('dateOfBirth')
        is_pilot = request.form.get('is_pilot')
        password1 = request.form.get('password1')
        confirmPassword = request.form.get('confirmPassword')

        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        is_pilot = bool(int(is_pilot))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != confirmPassword:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, password=password1, date_of_birth=dob, is_pilot=is_pilot)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
