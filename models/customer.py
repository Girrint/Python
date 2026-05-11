from models import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(50))

    email = db.Column(db.String(255))

    address = db.Column(db.Text)