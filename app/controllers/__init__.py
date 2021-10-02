import os
from flask import Blueprint, current_app

from app.controllers.alert_controller import index as alert_index
from app.controllers.alert_controller import alert_to_database
from app.controllers.alert_controller import alert_report

from app.controllers.snort_controller import index as snort_index
from app.controllers.snort_controller import snort_to_csv
from app.controllers.snort_controller import featurefortraining
from app.controllers.snort_controller import exe_featurefortraining

from app.controllers.abnormal_controller import training
from app.controllers.abnormal_controller import execute_training
from app.controllers.abnormal_controller import monitoring
from app.controllers.abnormal_controller import execute_monitoring
from app.controllers.abnormal_controller import info_alert
from app.controllers.abnormal_controller import testing
from app.controllers.abnormal_controller import execute_testing


template_dir = os.path.abspath('app/views')

alert_blueprints = Blueprint('alert', __name__, template_folder=template_dir)
alert_blueprints.add_url_rule('/', view_func=alert_index, methods=['GET'])
alert_blueprints.add_url_rule('/execute', endpoint='execute', view_func=alert_to_database, methods=['GET', 'POST'])
alert_blueprints.add_url_rule('/report', endpoint='report', view_func=alert_report, methods=['GET'])

snort_blueprints = Blueprint('snort', __name__, template_folder=template_dir)
snort_blueprints.add_url_rule('/', view_func=snort_index, methods=['GET'])
snort_blueprints.add_url_rule('/execute', endpoint='execute', view_func=snort_to_csv, methods=['GET', 'POST'])
snort_blueprints.add_url_rule('/featurefortraining', view_func=featurefortraining, methods=['GET'])
snort_blueprints.add_url_rule('/format', endpoint='format', view_func=exe_featurefortraining, methods=['GET', 'POST'])

abnormal_blueprints = Blueprint('abnormal', __name__, template_folder=template_dir)
abnormal_blueprints.add_url_rule('/training', endpoint='training', view_func=training, methods=['GET','POST'])
abnormal_blueprints.add_url_rule('/execute-training', endpoint='execute-training', view_func=execute_training, methods=['GET', 'POST'])
abnormal_blueprints.add_url_rule('/monitoring', endpoint='monitoring', view_func=monitoring, methods=['GET','POST'])
abnormal_blueprints.add_url_rule('/execute-monitoring', endpoint='execute-monitoring', view_func=execute_monitoring, methods=['GET', 'POST'])
abnormal_blueprints.add_url_rule('/info-alert', endpoint='info-alert', view_func=info_alert, methods=['GET'])
abnormal_blueprints.add_url_rule('/testing', endpoint='testing', view_func=testing, methods=['GET','POST'])
abnormal_blueprints.add_url_rule('/execute-testing', endpoint='execute-testing', view_func=execute_testing, methods=['GET', 'POST'])

