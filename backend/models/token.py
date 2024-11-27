from datetime import datetime
import time
import requests
from ..extensions import db

class StravaToken(db.Model):
    __tablename__ = 'strava_tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(255), nullable=False)
    refresh_token = db.Column(db.String(255), nullable=False)
    expires_at = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def get_valid_token(cls):
        """Get a valid token, refreshing if necessary."""
        token = cls.query.order_by(cls.created_at.desc()).first()
        
        if not token:
            return None
            
        # If token is expired or will expire in the next 5 minutes
        if token.expires_at < time.time() + 300:
            token.refresh()
            
        return token

    def refresh(self):
        """Refresh the access token using the refresh token."""
        from flask import current_app
        
        response = requests.post(
            'https://www.strava.com/oauth/token',
            data={
                'client_id': current_app.config['STRAVA_CLIENT_ID'],
                'client_secret': current_app.config['STRAVA_CLIENT_SECRET'],
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token
            }
        )
        
        if response.status_code != 200:
            raise Exception('Failed to refresh token')
            
        data = response.json()
        
        # Update token
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        self.expires_at = data['expires_at']
        
        db.session.commit()