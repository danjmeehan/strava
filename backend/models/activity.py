from datetime import datetime
from ..extensions import db

class Run(db.Model):
    __tablename__ = 'runs'
    
    id = db.Column(db.Integer, primary_key=True)
    strava_id = db.Column(db.BigInteger, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    moving_time = db.Column(db.Integer, nullable=False)
    elapsed_time = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    average_speed = db.Column(db.Float)
    max_speed = db.Column(db.Float)
    total_elevation_gain = db.Column(db.Float)
    average_cadence = db.Column(db.Float)
    elevation_high = db.Column(db.Float)
    elevation_low = db.Column(db.Float)
    start_latitude = db.Column(db.Float)
    start_longitude = db.Column(db.Float)
    end_latitude = db.Column(db.Float)
    end_longitude = db.Column(db.Float)
    average_temp = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.Column(db.Text)