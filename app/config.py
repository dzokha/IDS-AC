import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    YEAR_ALERT='2020'
    IP_SERVER = '192.168.1.100'
    IP_HONEYNET = '192.168.1.100'
    # IP not use for detect attack
    IP_FILTER = ['8.8.8.8','8.8.4.4','192.168.1.1']
    """Base config, uses staging database server."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('APP_SECRET_KEY') or os.urandom(24)
    UPLOAD_FOLDER = basedir + '/static/uploads'


    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = True
    DB_SERVER = '127.0.0.1'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost:3306/ids-ac-ver2'
    # """ Dealing with Disconnects """
    # # SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}
    # SQLALCHEMY_POOL_TIMEOUT = 1000000
    # SQLALCHEMY_POOL_SIZE = 100000
    # SQLALCHEMY_POOL_RECYCLE = 3600000
    # SQLALCHEMY_MAX_OVERFLOW = 1000000


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