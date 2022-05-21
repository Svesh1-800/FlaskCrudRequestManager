import os
from database import db
from project.models import Data, DataType
from auth.models import User
from setup import create_app,setup_database
from flask_migrate import Migrate
from project.views import table
from auth.views import auth
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
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






