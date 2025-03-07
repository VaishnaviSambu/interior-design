from datetime import datetime
from app import db

class DesignSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    room_type = db.Column(db.String(100), nullable=False)
    style_preference = db.Column(db.String(100), nullable=False)
    suggestion = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"DesignSuggestion('{self.customer_name}', '{self.room_type}', '{self.style_preference}')"
