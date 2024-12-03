from apscheduler.schedulers.background import BackgroundScheduler
from .routes.activities import sync_activities_task

scheduler = BackgroundScheduler()

def init_scheduler(app):
    def wrapped_task():
        with app.app_context():
            try:
                sync_activities_task()
            except Exception as e:
                print(f"Scheduler error: {str(e)}")

    scheduler.add_job(
        func=wrapped_task,
        trigger='interval',
        hours=12,
        id='sync_strava',
        max_instances=1
    )
    
    try:
        scheduler.start()
    except Exception as e:
        print(f"Error starting scheduler: {str(e)}")