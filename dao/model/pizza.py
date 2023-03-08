from marshmallow import fields, Schema

from pizza.setup_db import db


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    description = db.Column(db.String)
    pic = db.Column(db.String)

