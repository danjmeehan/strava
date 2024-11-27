from apscheduler.schedulers.background import BackgroundScheduler
from .routes.activities import sync_activities_task

scheduler = BackgroundScheduler()

def init_scheduler(app):
    def wrapped_task():
        with app.app_context():
            sync_activities_task()

    scheduler.add_job(
        func=wrapped_task,
        trigger='interval',
        minutes=1,  # For testing
        id='sync_strava',
        max_instances=1
    )
    
    scheduler.start()