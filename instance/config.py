import os
YEAR_ALERT='2020'
IP_SERVER = '192.168.1.100'
IP_HONEYNET = '192.168.1.100'
# IP not use for detect attack
IP_FILTER = ['8.8.8.8','8.8.4.4','192.168.1.1']

basedir = os.path.abspath(os.path.dirname(__file__))
parent=os.path.abspath(os.path.join(basedir,'..'))
UPLOAD_FOLDER = parent + '/app/static/uploads'
SECRET_KEY = os.environ.get('APP_SECRET_KEY') or os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost:3306/ids-ac-ver2'
# """ Dealing with Disconnects """
# # SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True} 
# SQLALCHEMY_POOL_TIMEOUT = 1000000
# SQLALCHEMY_POOL_SIZE = 100000
# SQLALCHEMY_POOL_RECYCLE = 3600000
# SQLALCHEMY_MAX_OVERFLOW = 1000000
SQLALCHEMY_TRACK_MODIFICATIONS = False
