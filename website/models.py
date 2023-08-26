from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pick_10 = db.Column(db.String(10000))
    pick_9 = db.Column(db.String(10000))
    pick_8 = db.Column(db.String(10000))
    pick_7 = db.Column(db.String(10000))
    pick_6 = db.Column(db.String(10000))
    pick_5 = db.Column(db.String(10000))
    pick_4 = db.Column(db.String(10000))
    pick_3 = db.Column(db.String(10000))
    pick_2 = db.Column(db.String(10000))
    pick_1 = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
