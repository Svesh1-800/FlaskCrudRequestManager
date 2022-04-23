import os, config
from flask import Flask

from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
   
    db.init_app(app)
   
    with app.app_context():
        db.create_all()

    
    
    return app

