from datetime import datetime
from flaskblog import db

class Visitor(db.Model):
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, primary_key = True)
    ph_number = db.Column(db.Integer(), nullable=False)
    check_in_time = db.Column(db.DateTime, default=datetime.now(), primary_key=True)
    check_out_time = db.Column(db.DateTime, default=None)


class Host(db.Model):
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, primary_key = True)
    ph_number = db.Column(db.Integer(), nullable=False, primary_key=True)
    address = db.Column(db.String(150), default='SummerGeeks')
