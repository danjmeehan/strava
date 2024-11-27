from flask import Blueprint, redirect, request, url_for, current_app
import requests
from urllib.parse import urlencode
from ..models.token import StravaToken
from .. import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    base_url = 'https://www.strava.com/oauth/authorize'
    params = {
        'client_id': current_app.config['STRAVA_CLIENT_ID'],
        'redirect_uri': 'http://127.0.0.1:5000/auth/callback',
        'response_type': 'code',
        'scope': 'read,activity:read_all',
        'approval_prompt': 'force'
    }
    
    authorization_url = f"{base_url}?{urlencode(params)}"
    print(f"Redirecting to: {authorization_url}")  # Debug print
    return redirect(authorization_url)

@bp.route('/callback')
def callback():
    code = request.args.get('code')
    
    response = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': current_app.config['STRAVA_CLIENT_ID'],
            'client_secret': current_app.config['STRAVA_CLIENT_SECRET'],
            'code': code,
            'grant_type': 'authorization_code'
        }
    )
    
    data = response.json()
    
    token = StravaToken(
        access_token=data['access_token'],
        refresh_token=data['refresh_token'],
        expires_at=data['expires_at']
    )
    
    db.session.add(token)
    db.session.commit()
    
    return "Authentication successful! Tokens have been stored."