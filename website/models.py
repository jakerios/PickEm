from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game1Pick = db.Column(db.String(10000))
    game2Pick = db.Column(db.String(10000))
    game3Pick = db.Column(db.String(10000))
    game4Pick = db.Column(db.String(10000))
    game5Pick = db.Column(db.String(10000))
    game6Pick = db.Column(db.String(10000))
    game7Pick = db.Column(db.String(10000))
    game8Pick = db.Column(db.String(10000))
    game9Pick = db.Column(db.String(10000))
    game10Pick = db.Column(db.String(10000))
    game11Pick = db.Column(db.String(10000))
    game12Pick = db.Column(db.String(10000))
    game13Pick = db.Column(db.String(10000))
    game14Pick = db.Column(db.String(10000))
    game15Pick = db.Column(db.String(10000))
    game16Pick = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
