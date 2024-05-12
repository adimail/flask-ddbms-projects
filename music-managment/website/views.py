from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Song, LikedSongs
from . import db
import json
from datetime import datetime
from flask import redirect, url_for

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        song = request.form.get('title') 
        release = request.form.get('release_date') 
        release = datetime.strptime(release, '%Y-%m-%d').date()
        new_song = Song(title=song, artist_id=current_user.id, release_date=release)
        db.session.add(new_song)
        db.session.commit()
        flash('Song added!', category='success')
        return redirect(url_for('views.home'))

    # Query all songs from the database
    all_songs = Song.query.all()
    liked_songs = [song.song_id for song in LikedSongs.query.filter_by(user_id=current_user.id).all()] 

    return render_template("home.html", user=current_user, songs=all_songs, liked_songs=liked_songs)



@views.route('/guest', methods=['GET'])
def guest():
    all_songs = Song.query.all()
    return render_template("guest.html", songs=all_songs, user=None)



@views.route('/delete-song', methods=['POST'])
def delete_song():
    data = json.loads(request.data)
    song_id = data['songId']
    song = Song.query.get(song_id)
    if song:
        if song.artist_id == current_user.id:
            db.session.delete(song)
            db.session.commit()
            flash('Song deleted!', category='danger')
        else:
            flash('song.artist_id != current_user.id!', category='danger')
    else:
        flash('No song!', category='danger')

    return jsonify({})


@views.route('/like/<int:song_id>', methods=['POST'])
@login_required
def like_song(song_id):
    song = Song.query.get(song_id)
    if song:
        already_liked = LikedSongs.query.filter_by(user_id=current_user.id, song_id=song_id).first()
        if already_liked:
            pass
        else:
            new_liked_song = LikedSongs(user_id=current_user.id, song_id=song_id)
            db.session.add(new_liked_song)
            db.session.commit()
    
    return redirect(url_for('views.home'))

@views.route('/unlike/<int:song_id>', methods=['POST'])
@login_required
def unlike_song(song_id):
    song = Song.query.get(song_id)
    if song:
        liked_song = LikedSongs.query.filter_by(user_id=current_user.id, song_id=song_id).first()
        if liked_song:
            db.session.delete(liked_song)
            db.session.commit()
    
    return redirect(url_for('views.home'))
