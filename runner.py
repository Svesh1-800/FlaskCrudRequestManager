import os
from database import db
from project.models import Data, DataType
from project import create_app,setup_database
from flask_migrate import Migrate
from project.views import table
from auth.views import auth



app = create_app()
if not os.path.isfile('/test.db'):
    setup_database(app)
migrate = Migrate(app,db)
app.register_blueprint(table)
app.register_blueprint(auth)
app.run()
@app.shell_context_processor
def make_shell_context():
    return {'db': db,'Data':Data,'DataType':DataType}






