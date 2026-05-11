from datetime import datetime
from models import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    status = db.Column(db.String(50), default='pending')

    total_price = db.Column(db.Float, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    customer = db.relationship('Customer', backref='orders')