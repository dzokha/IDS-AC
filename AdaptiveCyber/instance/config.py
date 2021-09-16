import os
basedir = os.path.abspath(os.path.dirname(__file__))
parent=os.path.abspath(os.path.join(basedir,'..'))
UPLOAD_FOLDER = parent + '/app/static/uploads'
SECRET_KEY = os.environ.get('APP_SECRET_KEY') or os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost:3306/adaptivecyber'
SQLALCHEMY_TRACK_MODIFICATIONS = False
