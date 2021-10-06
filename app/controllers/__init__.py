import os
from flask import Blueprint, current_app

from app.controllers.alert_controller import index as alert_index
from app.controllers.alert_controller import alert_to_database
from app.controllers.alert_controller import alert_report
from app.controllers.alert_controller import alert_fix_country


template_dir = os.path.abspath('app/views')

alert_blueprints = Blueprint('alert', __name__, template_folder=template_dir)
alert_blueprints.add_url_rule('/', view_func=alert_index, methods=['GET'])
alert_blueprints.add_url_rule('/execute', endpoint='execute', view_func=alert_to_database, methods=['GET', 'POST'])
alert_blueprints.add_url_rule('/report', endpoint='report', view_func=alert_report, methods=['GET'])
alert_blueprints.add_url_rule('/fix-country', endpoint='fix-country', view_func=alert_fix_country, methods=['GET'])