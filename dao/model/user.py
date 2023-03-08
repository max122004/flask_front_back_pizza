from pizza.setup_db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    fio = db.Column(db.String)
    number = db.Column(db.Integer)
    email = db.Column(db.String)
    address = db.Column(db.String)