from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.models import alert
from app.models import snort
from app.models import abnormal