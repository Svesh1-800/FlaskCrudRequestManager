import os

from flask_migrate import Migrate

from project import create_app
from project.views import crud_requests
from project.database import db
app = create_app()

app.register_blueprint(crud_requests)
app.app_context().push()

migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run()