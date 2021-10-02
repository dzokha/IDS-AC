name="ids-ac"


import os
# third-party imports
from flask import Flask


from flask_migrate import Migrate

# local imports
from app.config import app_config
from app.models import db
# import blueprints
from app.routes import routes
from app.controllers import alert_blueprints
from app.controllers import snort_blueprints
from app.controllers import abnormal_blueprints



# app.config.from_object('yourapplication.default_settings')
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')



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

	# database
	db.init_app(app)
	migrate = Migrate(app,db)

	# register blueprints
	app.register_blueprint(routes)
	app.register_blueprint(alert_blueprints, url_prefix='/alert')
	app.register_blueprint(snort_blueprints, url_prefix='/snort')
	app.register_blueprint(abnormal_blueprints, url_prefix='/abnormal')
	return app