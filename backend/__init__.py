from flask import Flask
from .extensions import db, migrate
from .config import Config
from .scheduler import init_scheduler

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from .models.activity import Run
    from .models.token import StravaToken

    # Register blueprints
    from .routes.auth import bp as auth_bp
    from .routes.activities import bp as activities_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(activities_bp)

    init_scheduler(app)

    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200

    return app