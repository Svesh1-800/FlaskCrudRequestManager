import os
import config
from database import db
from project.models import Data, DataType
from auth.models import User
from flask import Flask
from flask_migrate import Migrate
from project.views import table
from auth.views import auth
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    db.init_app(app)
    return app
def setup_database(app):
    with app.app_context():
        db.create_all()

# need to add csrf
app = create_app()
if not os.path.isfile('/test.db'):
    setup_database(app)
migrate = Migrate(app,db)
app.register_blueprint(table)
app.register_blueprint(auth)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.shell_context_processor
def make_shell_context():
    return {'db': db,'Data':Data,'DataType':DataType, 'User': User}






