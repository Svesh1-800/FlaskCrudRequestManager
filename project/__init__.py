from database import db
from flask import Flask
import os
import config




def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    db.init_app(app)
    return app
def setup_database(app):
    with app.app_context():
        db.create_all()
