from project.database import db
from flask import Flask
from project.models import Data, DataType
import os
import config
from project.views import table
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    db.init_app(app)
    migrate = Migrate(app,db)
    app.register_blueprint(table)
    return app
def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    if not os.path.isfile('/test.db'):
        setup_database(app)
    
    app.run()

