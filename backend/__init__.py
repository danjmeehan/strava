from flask import Flask
from flask_cors import CORS
from .extensions import db
from .routes.activities import bp as activities_bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    
    # Simpler CORS configuration - allow all origins for now
    CORS(app)
    
    # Database configuration
    DB_USER = 'danjmeehan'
    DB_PASSWORD = 'Tra1n1ng!'
    DB_NAME = 'training'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Register blueprints
    app.register_blueprint(activities_bp)
    
    return app