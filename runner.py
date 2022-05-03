""" import os

from flask_migrate import Migrate

from project import create_app
from project.views import crud_requests
from project.database import db
app = create_app()

app.register_blueprint(crud_requests)
app.app_context().push()

migrate = Migrate(app,db,render_as_batch=True)

if __name__ == '__main__':
    app.run() """
from project.database import db
from flask import Flask
import os
import config
from project.views import table

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    db.init_app(app)
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
