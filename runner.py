import os


from project import create_app
from project.views import crud_requests
app = create_app()
app.register_blueprint(crud_requests)
    



if __name__ == '__main__':
    app.run()