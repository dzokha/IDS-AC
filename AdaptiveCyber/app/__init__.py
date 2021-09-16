import os
from flask import Flask

from flask_migrate import Migrate
from app.config import app_config
from app.models.models import db
from app.routes import routes
from app.controllers import user_blueprints
from app.controllers import alert_blueprints
from app.controllers import tcpdump_blueprints
from app.controllers import deepmg_blueprints

def create_app(config_name=None):
	app = Flask(__name__, instance_relative_config=True)

	if config_name is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_object(app_config[config_name])

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	
	db.init_app(app)


	migrate = Migrate(app,db)
	from app.models import models

	# register blueprints
	app.register_blueprint(routes)
	app.register_blueprint(user_blueprints)
	app.register_blueprint(alert_blueprints, url_prefix='/alert')
	app.register_blueprint(tcpdump_blueprints, url_prefix='/tcpdump')
	app.register_blueprint(deepmg_blueprints, url_prefix='/deepmg')
	return app