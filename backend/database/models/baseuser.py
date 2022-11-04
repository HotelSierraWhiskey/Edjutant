from ..db import db


class BaseUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    admin =  db.Column(db.Boolean)
    instructor = db.Column(db.Boolean)
