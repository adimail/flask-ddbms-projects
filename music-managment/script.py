from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nqMt+o1BxO2Wkaj4ogmFtg=='
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    is_artist = db.Column(db.Boolean, nullable=False)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

dummy_user_data = [
    ('lanadelrey@example.com', 'admin', 'Lana Del Rey', '1985-06-21', True),
    ('jamesbay@example.com', 'admin', 'James Bay', '1990-09-04', True),
    ('arcticmonkeys@example.com', 'admin', 'Arctic Monkeys', '1986-01-28', True),
    ('sia@example.com', 'admin', 'Sia', '1975-12-18', True),
    ('prateekkuhad@example.com', 'admin', 'Prateek Kuhad', '1990-11-03', True),
    ('joji@example.com', 'admin', 'Joji', '1992-09-18', True),
    ('adele@example.com', 'admin', 'Adele', '1988-05-05', True),
    ('acdc@example.com', 'admin', 'AC/DC', '1973-11-19', True),
    ('amittrivedi@example.com', 'admin', 'Amit Trivedi', '1979-07-08', True),
    ('brunomars@example.com', 'admin', 'Bruno Mars', '1985-10-08', True),
    ('lorde@example.com', 'admin', 'Lorde', '1996-11-07', True),
    ('shakira@example.com', 'admin', 'Shakira', '1977-02-02', True),
    ('taylorswift@example.com', 'admin', 'Taylor Swift', '1989-12-13', True),
    ('atifaslam@example.com', 'admin', 'Atif Aslam', '1983-03-12', True),
    ('radiohead@example.com', 'admin', 'Radiohead', '1985-02-17', True),
    ('katyperry@example.com', 'admin', 'Katy Perry', '1984-10-25', True),
    ('eminem@example.com', 'admin', 'Eminem', '1972-10-17', True),
    ('queen@example.com', 'admin', 'Queen', '1970-07-19', True),
    ('kanyewest@example.com', 'admin', 'Kanye West', '1977-06-08', True),
    ('pinkfloyd@example.com', 'admin', 'Pink Floyd', '1965-03-06', True),
    ('michaeljackson@example.com', 'admin', 'Michael Jackson', '1958-08-29', True),
    ('arianagrande@example.com', 'admin', 'Ariana Grande', '1993-06-26', True),
    ('postmalone@example.com', 'admin', 'Post Malone', '1995-07-04', True),
    ('tupac@example.com', 'admin', 'Tupac Shakur', '1971-06-16', True),
    ('fleetwoodmac@example.com', 'admin', 'Fleetwood Mac', '1967-07-11', True),
    ('ledzeppelin@example.com', 'admin', 'Led Zeppelin', '1968-07-24', True),
    ('snoopdogg@example.com', 'admin', 'Snoop Dogg', '1971-10-20', True),
    ('thechainsmokers@example.com', 'admin', 'The Chainsmokers', '1985-09-14', True),
    ('bobmarley@example.com', 'admin', 'Bob Marley', '1945-02-06', True),
    ('whitneyhouston@example.com', 'admin', 'Whitney Houston', '1963-08-09', True),
    ('eltonjohn@example.com', 'admin', 'Elton John', '1947-03-25', True),
    ('nirvana@example.com', 'admin', 'Nirvana', '1967-01-07', True)
]

dummy_song_data = [
    ("Born to Die", "2012-01-27", 2),
    ("Summertime Sadness", "2012-06-22", 2),
    ("Video Games", "2011-10-07", 2),
    ("Doin Time", "2019-05-17", 2),
    ("Blue Jeans", "2012-04-08", 2),
    ("Let It Go", "2014-09-16", 3),
    ("Hold Back the River", "2014-03-17", 3),
    ("Scars", "2015-03-23", 3),
    ("Us", "2014-05-18", 3),
    ("If You Ever Want to Be in Love", "2015-03-23", 3),
    ("Do I Wanna Know?", "2013-06-19", 4),
    ("R U Mine?", "2012-02-27", 4),
    ("I Bet You Look Good on the Dancefloor", "2005-10-17", 4),
    ("505", "2007-07-18", 4),
    ("Fluorescent Adolescent", "2007-07-09", 4),
    ("Chandelier", "2014-03-17", 5),
    ("Cheap Thrills", "2016-01-29", 5),
    ("Elastic Heart", "2013-09-23", 5),
    ("The Greatest", "2016-09-06", 5),
    ("Alive", "2015-09-25", 5),
    ("cold/mess", "2018-07-27", 6),
    ("Kadam", "2016-12-17", 6),
    ("Raat Raazi", "2018-07-27", 6),
    ("Tum Jab Paas", "2016-12-17", 6),
    ("Tune Kaha", "2018-07-27", 6),
    ("Slow Dancing in the Dark", "2018-09-12", 7),
    ("SLOW DANCING IN THE DARK (Acoustic)", "2018-12-18", 7),
    ("Yeah Right", "2018-05-17", 7),
    ("Test Drive", "2018-10-12", 7),
    ("Will He", "2017-10-17", 7),
    ("Someone Like You", "2011-02-21", 8),
    ("Rolling in the Deep", "2010-11-29", 8),
    ("Hello", "2015-10-23", 8),
    ("Set Fire to the Rain", "2011-11-21", 8),
    ("Skyfall", "2012-10-05", 8),
    ("Highway to Hell", "1979-07-27", 9),
    ("Thunderstruck", "1990-09-10", 9),
    ("Back in Black", "1980-07-25", 9),
    ("You Shook Me All Night Long", "1980-07-19", 9),
    ("T.N.T.", "1975-12-01", 9),
    ("Iktara", "2009-08-07", 10),
    ("Nayan Tarse", "2019-10-18", 10),
    ("Manmarziyan", "2018-08-14", 10),
    ("Sham", "2019-10-07", 10),
    ("Udta Punjab", "2016-04-18", 10),
    ("Grenade", "2010-09-28", 11),
    ("Just the Way You Are", "2010-07-20", 11),
    ("Locked Out of Heaven", "2012-10-01", 11),
    ("24K Magic", "2016-10-07", 11),
    ("The Lazy Song", "2011-02-15", 11),
    ("Royals", "2013-06-03", 12),
    ("Team", "2013-09-13", 12),
    ("Green Light", "2017-03-02", 12),
    ("Perfect Places", "2017-06-02", 12),
    ("Tennis Court", "2013-06-07", 12),
    ("Hips Dont Lie", "2006-02-28", 13),
    ("Whenever, Wherever", "2001-08-27", 13),
    ("Waka Waka (This Time for Africa)", "2010-05-07", 13),
    ("La Tortura", "2005-04-12", 13),
    ("Try Everything", "2016-01-08", 13),
    ("Love Story", "2008-09-12", 14),
    ("Shake It Off", "2014-08-18", 14),
    ("Blank Space", "2014-08-18", 14),
    ("You Belong with Me", "2008-11-11", 14),
    ("Bad Blood", "2015-05-17", 14),
    ("Tera Hone Laga Hoon", "2009-04-21", 15),
    ("Jeene Laga Hoon", "2013-01-15", 15),
    ("Tere Sang Yaara", "2016-06-06", 15),
    ("Dil Diyan Gallan", "2017-12-02", 15),
    ("Pehli Dafa", "2017-01-06", 15),
    ("Creep", "1992-09-21", 16),
    ("Karma Police", "1997-06-16", 16),
    ("Fake Plastic Trees", "1995-05-15", 16),
    ("No Surprises", "1998-01-12", 16),
    ("High and Dry", "1995-03-27", 16),
    ("Firework", "2010-10-26", 17),
    ("Roar", "2013-08-10", 17),
    ("California Gurls", "2010-05-07", 17),
    ("Dark Horse", "2013-09-17", 17),
    ("Teenage Dream", "2010-08-24", 17),
    ("Lose Yourself", "2002-10-22", 18),
    ("Without Me", "2002-05-14", 18),
    ("Love the Way You Lie", "2010-06-18", 18),
    ("Stan", "2000-11-21", 18),
    ("The Real Slim Shady", "2000-05-16", 18),
    ("Bohemian Rhapsody", "1975-10-31", 19),
    ("Dont Stop Me Now", "1978-01-27", 19),
    ("Somebody to Love", "1976-11-12", 19),
    ("We Will Rock You", "1977-10-07", 19),
    ("Another One Bites the Dust", "1980-06-30", 19),
    ("Stronger", "2007-07-31", 20),
    ("Heartless", "2008-11-04", 20),
    ("Gold Digger", "2005-07-05", 20),
    ("Jesus Walks", "2004-05-25", 20),
    ("All of the Lights", "2010-11-22", 20),
    ("Comfortably Numb", "1979-11-30", 21),
    ("Wish You Were Here", "1975-09-12", 21),
    ("Time", "1973-03-01", 21),
    ("Another Brick in the Wall", "1979-11-30", 21),
    ("Money", "1973-03-01", 21),
    ("Billie Jean", "1983-01-02", 22),
    ("Thriller", "1982-11-30", 22),
    ("Beat It", "1983-02-14", 22),
    ("Smooth Criminal", "1988-10-21", 22),
    ("Man in the Mirror", "1987-01-09", 22),
    ("Thank U, Next", "2018-11-03", 23),
    ("7 Rings", "2019-01-18", 23),
    ("No Tears Left to Cry", "2018-04-20", 23),
    ("Break Free", "2014-07-02", 23),
    ("Problem", "2014-04-28", 23),
    ("Circles", "2019-08-30", 24),
    ("Rockstar", "2017-09-15", 24),
    ("Congratulations", "2016-11-04", 24),
    ("Sunflower", "2018-10-18", 24),
    ("Better Now", "2018-04-27", 24),
    ("California Love", "1995-12-28", 25),
    ("Changes", "1998-10-13", 25),
    ("Dear Mama", "1995-02-21", 25),
    ("Hit Em Up", "1996-06-04", 25),
    ("Ghetto Gospel", "2004-11-29", 25),
    ("Go Your Own Way", "1976-12-03", 26),
    ("Dreams", "1977-02-04", 26),
    ("The Chain", "1977-02-04", 26),
    ("Rhiannon", "1975-02-04", 26),
    ("Landslide", "1975-07-11", 26),
    ("Stairway to Heaven", "1971-11-08", 27),
    ("Whole Lotta Love", "1969-10-22", 27),
    ("Kashmir", "1975-02-24", 27),
    ("Immigrant Song", "1970-11-05", 27),
    ("Black Dog", "1971-11-08", 27),
    ("Gin and Juice", "1994-11-15", 28),
    ("Drop It Like Its Hot", "2004-09-12", 28),
    ("Young, Wild & Free", "2011-10-11", 28),
    ("Who Am I (Whats My Name)?", "1993-10-31", 28),
    ("Beautiful", "2002-01-21", 28),
    ("Closer", "2016-07-29", 29),
    ("Dont Let Me Down", "2016-02-05", 29),
    ("Something Just Like This", "2017-02-22", 29),
    ("Roses", "2015-06-16", 29),
    ("Paris", "2017-01-13", 29),
    ("Three Little Birds", "1977-06-03", 30),
    ("No Woman, No Cry", "1975-10-01", 30),
    ("Redemption Song", "1980-10-02", 30),
    ("Could You Be Loved", "1980-05-29", 30),
    ("One Love / People Get Ready", "1965-12-10", 30),
    ("I Will Always Love You", "1992-11-03", 31),
    ("I Wanna Dance with Somebody (Who Loves Me)", "1987-05-02", 31),
    ("Greatest Love of All", "1985-03-18", 31),
    ("How Will I Know", "1985-11-22", 31),
    ("Saving All My Love for You", "1985-08-13", 31),
    ("Rocket Man", "1972-04-28", 32),
    ("Your Song", "1970-10-26", 32),
    ("Tiny Dancer", "1971-02-07", 32),
    ("Bennie and the Jets", "1974-02-04", 32),
    ("Goodbye Yellow Brick Road", "1973-10-05", 32),
    ("Smells Like Teen Spirit", "1991-09-10", 33),
    ("Come as You Are", "1991-09-24", 33),
    ("Lithium", "1992-07-13", 33),
    ("Heart-Shaped Box", "1993-08-30", 33),
    ("In Bloom", "1991-11-30", 33)
]

# Insert dummy users into the database
for email, password, name, dob, is_artist in dummy_user_data:
    user = User(
        email=email,
        password=password,
        name=name,
        date_of_birth=datetime.strptime(dob, '%Y-%m-%d').date(),
        is_artist=is_artist
    )
    db.session.add(user)

db.session.commit()

# Insert dummy songs into the database
for title, release_date, artist_id in dummy_song_data:
    song = Song(
        title=title,
        release_date=datetime.strptime(release_date, '%Y-%m-%d').date(),
        artist_id=artist_id
    )
    db.session.add(song)

db.session.commit()