from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Song
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

    return render_template("home.html", user=current_user, songs=all_songs)


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

    return jsonify({})