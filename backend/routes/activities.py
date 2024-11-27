from flask import Blueprint, jsonify, request
import requests
from ..models.token import StravaToken
from ..models.activity import Run
from .. import db
from datetime import datetime, timedelta
from sqlalchemy import func, cast, Numeric

bp = Blueprint('activities', __name__, url_prefix='/activities')

@bp.route('/sync')
def sync_activities():
    token = StravaToken.get_valid_token()
    
    if not token:
        return jsonify({'error': 'No token found. Please authenticate first.'}), 401
    
    new_activities = 0
    page = 1
    per_page = 100
    
    while True:
        try:
            headers = {'Authorization': f'Bearer {token.access_token}'}
            response = requests.get(
                'https://www.strava.com/api/v3/athlete/activities',
                headers=headers,
                params={
                    'page': page,
                    'per_page': per_page
                }
            )
            
            if response.status_code == 401:
                token = StravaToken.get_valid_token()
                continue
                
            if response.status_code != 200:
                return jsonify({'error': 'Failed to fetch activities from Strava'}), 400
                
            activities = response.json()
            
            # If no more activities, break the loop
            if not activities:
                break
                
            for activity in activities:
                # Only process runs
                if activity['type'] != 'Run':
                    continue
                    
                # Check if activity already exists
                existing = Run.query.filter_by(strava_id=activity['id']).first()
                if existing:
                    continue
                    
                # Create new run
                run = Run(
                    strava_id=activity['id'],
                    name=activity['name'],
                    distance=activity['distance'],
                    moving_time=activity['moving_time'],
                    elapsed_time=activity['elapsed_time'],
                    start_date=datetime.strptime(activity['start_date'], '%Y-%m-%dT%H:%M:%SZ'),
                    average_speed=activity['average_speed'],
                    max_speed=activity['max_speed'],
                    total_elevation_gain=activity['total_elevation_gain'],
                    average_cadence=activity.get('average_cadence'),
                    elevation_high=activity.get('elev_high'),
                    elevation_low=activity.get('elev_low'),
                    start_latitude=activity['start_latlng'][0] if activity.get('start_latlng') else None,
                    start_longitude=activity['start_latlng'][1] if activity.get('start_latlng') else None,
                    end_latitude=activity['end_latlng'][0] if activity.get('end_latlng') else None,
                    end_longitude=activity['end_latlng'][1] if activity.get('end_latlng') else None,
                    average_temp=activity.get('average_temp')
                )
                
                db.session.add(run)
                new_activities += 1
            
            # Move to next page
            page += 1
            
            # Commit after each page to avoid large transactions
            db.session.commit()
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'message': f'Successfully synced {new_activities} new activities'
    })

def sync_activities_task():
    """Version of sync_activities that runs as a background task"""
    print(f"\n{'='*50}")
    print(f"Scheduler: Starting activity sync at {datetime.now()}")
    
    token = StravaToken.get_valid_token()
    if not token:
        print("No valid token found")
        return
    
    new_activities = 0
    page = 1
    per_page = 100
    
    while True:
        try:
            headers = {'Authorization': f'Bearer {token.access_token}'}
            response = requests.get(
                'https://www.strava.com/api/v3/athlete/activities',
                headers=headers,
                params={
                    'page': page,
                    'per_page': per_page
                }
            )
            
            if response.status_code == 401:
                token = StravaToken.get_valid_token()
                continue
                
            if response.status_code != 200:
                print(f"Failed to fetch activities: {response.status_code}")
                return
                
            activities = response.json()
            
            if not activities:
                break
                
            for activity in activities:
                # Only process runs
                if activity['type'] != 'Run':
                    continue
                    
                # Check if activity already exists
                existing = Run.query.filter_by(strava_id=activity['id']).first()
                if existing:
                    continue
                    
                # Create new run
                run = Run(
                    strava_id=activity['id'],
                    name=activity['name'],
                    distance=activity['distance'],
                    moving_time=activity['moving_time'],
                    elapsed_time=activity['elapsed_time'],
                    start_date=datetime.strptime(activity['start_date'], '%Y-%m-%dT%H:%M:%SZ'),
                    average_speed=activity['average_speed'],
                    max_speed=activity['max_speed'],
                    total_elevation_gain=activity['total_elevation_gain'],
                    average_cadence=activity.get('average_cadence'),
                    elevation_high=activity.get('elev_high'),
                    elevation_low=activity.get('elev_low'),
                    start_latitude=activity['start_latlng'][0] if activity.get('start_latlng') else None,
                    start_longitude=activity['start_latlng'][1] if activity.get('start_latlng') else None,
                    end_latitude=activity['end_latlng'][0] if activity.get('end_latlng') else None,
                    end_longitude=activity['end_latlng'][1] if activity.get('end_latlng') else None,
                    average_temp=activity.get('average_temp')
                )
                
                db.session.add(run)
                new_activities += 1
            
            # Move to next page
            page += 1
            
            # Commit after each page to avoid large transactions
            db.session.commit()
            
        except Exception as e:
            print(f"Error syncing activities: {str(e)}")
            return

@bp.route('/stats/weekly')
def get_weekly_mileage():
    """Get total distance per week"""
    try:
        # Get parameters with defaults
        weeks = request.args.get('weeks', 52, type=int)  # Default to 1 year
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(weeks=weeks)
        
        # Query weekly totals
        weekly_stats = db.session.query(
            func.date_trunc('week', Run.start_date).label('week'),
            # Use cast to numeric for proper rounding
            func.round(
                cast(func.sum(Run.distance) * 0.000621371, Numeric(10, 2))
            ).label('miles')
        ).filter(
            Run.start_date >= start_date,
            Run.start_date <= end_date
        ).group_by(
            func.date_trunc('week', Run.start_date)
        ).order_by(
            'week'
        ).all()
        
        # Format the results
        results = [{
            'week': week.strftime('%Y-%m-%d'),
            'miles': float(miles) if miles is not None else 0
        } for week, miles in weekly_stats]
        
        return jsonify(results)
        
    except Exception as e:
        print(f"Error in get_weekly_mileage: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500