from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Song, LikedSongs
from . import db   ##means from __init__.py import db
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
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
    if request.method == 'POST': 
        song = request.form.get('title') 
        release = request.form.get('release_date') 
        release = datetime.strptime(release, '%Y-%m-%d').date()
        new_song = Song(title=song, artist_id=current_user.id, release_date=release)
        db.session.add(new_song)
        db.session.commit()
        flash('Song added!', category='success')

    all_songs = Song.query.all()
    liked_songs = [song.song_id for song in LikedSongs.query.filter_by(user_id=current_user.id).all()] 

    return render_template("profile.html", user=current_user, songs=all_songs, liked_songs=liked_songs)


@auth.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    all_songs = Song.query.all()
    liked_songs = [song.song_id for song in LikedSongs.query.filter_by(user_id=current_user.id).all()] 
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            search_results = Song.query.filter(
                (Song.title.ilike(f"%{search_query}%")) |
                (Song.artist.has(User.name.ilike(f"%{search_query}%")))
            ).all()
            return render_template("search.html", user=current_user, search_results=search_results, songs=all_songs, liked_songs=liked_songs)

    return render_template("search.html", user=current_user, search_results=None, songs=all_songs, liked_songs=liked_songs)

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
        artist = request.form.get('isArtist')
        password1 = request.form.get('password1')
        confirmPassword = request.form.get('confirmPassword')

        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        is_artist = bool(int(artist))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != confirmPassword:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, password=password1, date_of_birth=dob, is_artist=is_artist)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)