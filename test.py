import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from sqlalchemy.ext.associationproxy import association_proxy

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:passwort@localhost:5432/testy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key = True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key = True)
    start_time = db.Column(db.DateTime, nullable = False)
    artist = db.relationship('Artist', backref = db.backref('shows', cascade = "all, delete-orphan"))
    venue = db.relationship('Venue', backref = db.backref('shows', cascade = "all, delete-orphan"))



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_description = db.Column(db.String)
    seeking_talent = db.Column(db.Boolean, default = True)

    artists = association_proxy('shows', 'artist' , cascade_scalar_deletes= True)


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_description = db.Column(db.String)
    seeking_venue = db.Column(db.Boolean, default = True)
    website = db.Column(db.String(120))

    venues = association_proxy('shows', 'venue' , cascade_scalar_deletes= True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.



# db.drop_all()
db.create_all()



if __name__ == '__main__':
    app.run()
