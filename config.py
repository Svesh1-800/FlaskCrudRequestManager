import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

   


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or 'sqlite:///' + os.path.join(app_dir,'test.db')
class TestingConfig(BaseConfig):
    DEBUG = True
    


class ProductionConfig(BaseConfig):
    DEBUG = False