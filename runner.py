import os
from project.database import db
from project.models import Data, DataType
from project import create_app,setup_database
from flask_migrate import Migrate



app = create_app()
if not os.path.isfile('/test.db'):
    setup_database(app)
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return {'db': db,'Data':Data,'DataType':DataType}
app.run()






