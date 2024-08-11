

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from pathlib import Path

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    Path("catpure_data_error").mkdir(parents=True, exist_ok=True)
    Path("logs").mkdir(parents=True, exist_ok=True)

    # Basic logging configuration
    logging.basicConfig(level=logging.INFO,  # Adjust the logging level as needed
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler('logs/app.log'),  # Log to a file
                            logging.StreamHandler()  # Also log to the console
                        ])
    
    app.logger.info('Creating Flask app')

    db.init_app(app)
    migrate.init_app(app, db)


    from app.api.views import api  # Import views
    app.register_blueprint(api)

    return app
