import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('APP_SECRET_KEY') or os.urandom(24)
    UPLOAD_FOLDER = basedir + '/static/uploads'


    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = True
    DB_SERVER = '127.0.0.1'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost:3306/adaptivecyber'


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'

class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True

class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///tcpfeature.sqlite"

app_config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing':TestingConfig
}