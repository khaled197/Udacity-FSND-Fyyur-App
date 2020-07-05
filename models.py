from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
    start_time = db.Column(db.DateTime, nullable = False, primary_key=True)
    artist = db.relationship('Artist', backref = db.backref('shows', cascade = "all, delete-orphan"))
    venue = db.relationship('Venue', backref = db.backref('shows', cascade = "all, delete-orphan"))



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    address = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.String(120), nullable = False)
    facebook_link = db.Column(db.String(120), nullable = False)
    website = db.Column(db.String(120))
    seeking_description = db.Column(db.String)
    seeking_talent = db.Column(db.Boolean, default = True)

    artists = association_proxy('shows', 'artist' , cascade_scalar_deletes= True)


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120), nullable = False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), nullable = False)
    seeking_description = db.Column(db.String)
    seeking_venue = db.Column(db.Boolean, default = True)
    website = db.Column(db.String(120))

    venues = association_proxy('shows', 'venue' , cascade_scalar_deletes= True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
