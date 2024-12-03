from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate, cors
from .config import Config
from .routes.activities import bp as activities_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Database configuration
    DB_USER = 'danjmeehan'
    DB_PASSWORD = 'Tra1n1ng!'
    DB_NAME = 'training'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(activities_bp)
    
    return app