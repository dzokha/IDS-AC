import os, sys
import json
if sys.version_info[0] < 3:
	from urllib2 import urlopen
else:
	from urllib.request import urlopen
from flask import current_app, flash, request, jsonify, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from app.models import db
from app.models.alert import Alert
from sqlalchemy import func
from sqlalchemy import exc
import sqlalchemy.pool as pool

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@user_blueprints.route('/alert')
def index():
	result = db.session.query(Alert.priority, Alert.classification, Alert.msg, func.count(Alert.msg)).group_by(Alert.priority, Alert.classification,Alert.msg).all()
	return render_template("alert/index.html", alert=result)


#@user_blueprints.route('/execute', method="POST")
def alert_to_database():
	""" run csvalert"""
	year_alert = current_app.config["YEAR_ALERT"]
	ip_filter = current_app.config["IP_FILTER"]
	ip_honeynet = current_app.config["IP_HONEYNET"]
	# Create a directory in a known location to save files to.
	uploads_dir = os.path.join(current_app.config["UPLOAD_FOLDER"], 'alert')
	os.makedirs(uploads_dir, exist_ok = True)

	if request.method == 'POST':
		multifile = request.files.getlist('path[]')
		if multifile:
			for file in multifile:
				file_name = secure_filename(file.filename)
				file.save(os.path.join(uploads_dir, file_name))
			for file in multifile:
				file_name = secure_filename(file.filename)
				file_log = uploads_dir + '/'+file_name

				with open(file_log) as multi_line:
					four_line = error_line = 0
					for line in multi_line:
						try:
							if four_line == 0:
								gid_sid_rev = msg = classification = \
								date_time = loc = country = \
								src_ip = dst_ip = meta_data = ""
								priority = timestamp = src_port = dst_port = 0
							four_line += 1
							if not line.strip() and four_line > 3:
								four_line = 0
								if error_line == 1:
									error_line = 0
									continue
								if src_ip in ip_filter or dst_ip in ip_filter:
									continue
								if date_time != "":
									if src_ip == ip_honeynet or dst_ip == ip_honeynet:
										exists = db.session.query(Alert.id).filter_by(date_time=date_time).first()
										if exists is None:
											record = Alert(gid_sid_rev, msg, classification, priority, timestamp, date_time,src_ip,src_port,dst_ip,dst_port,meta_data)
											db.session.add(record)
											db.session.commit()
										# else:
										# 	print('Double key')
										# 	break
							else:
								str_line = line.strip()
								if four_line == 1:
									first_line = str_line.split(" ",2)
									msg = first_line[2].split("[**]")[0]
									gid_sid_rev = first_line[1]
								if four_line == 2:
									second_line = str_line.split("]")
									if len(second_line) < 3:
										error_line = 1
										continue
									classification = second_line[0].split(":")[1]
									priority = second_line[1].split(":")[1]
								if four_line == 3:
									if error_line == 1:
										continue
									three_line = str_line.split(" ")
									timestamp_str = three_line[0].split("-")
									timestamp_date = timestamp_str[0].split("/")
									date_time = year_alert + '-' + timestamp_date[0] + '-' + timestamp_date[1] + ' ' + timestamp_str[1]
									timestamp = int(datetime.timestamp(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')) * 1000)
									src = three_line[1].split(":")
									if len(src) < 2:
										error_line = 1
										continue
									src_ip = src[0]
									src_port = src[1]
									dst = three_line[3].split(":")
									if len(dst) < 2:
										error_line = 1
										continue
									dst_ip = dst[0]
									dst_port = dst[1]
								if four_line > 3:
									meta_data = meta_data + " " + str_line

						except Exception as ex:
							# deplay = input('Enter for continue.\n')
							print(ex)

			flash(str(multifile),'success')
			return redirect(url_for('alert.index', filename=file_name))
		else:
			flash('No file chosen','warning')
			return redirect(request.url)
	return redirect(url_for('alert.index'))


#@user_blueprints.route('/report, method="GET")
def alert_report():
	result = db.session.query(Alert.loc, Alert.country).where(Alert.country != None).distinct().all()
	country_null = db.session.query(func.count(Alert.src_ip.distinct())).filter(Alert.country.is_(None)).first()
	country = country_null[0] - 1
	return render_template("alert/report.html", alert=result, country=country)

#@user_blueprints.route('/fix-country, method="GET")
def alert_fix_country():
	try:
		ip_filter = current_app.config["IP_FILTER"]
		ip_honeynet = current_app.config["IP_HONEYNET"]
		result = db.session.query(Alert.dst_ip).where(Alert.country == None).distinct().all()
		for row in result:
			ip = row[0]
			if ip != ip_honeynet and ip not in ip_filter:
				ipmap = 'http://ipinfo.io/' + ip +'/json'
				response = urlopen(ipmap).read()
				json_data = json.loads(response)
				loc = json_data.get('loc')
				country = json_data.get('country')

				db.session.query(Alert).filter((Alert.dst_ip.like(ip)) | (Alert.src_ip.like(ip))).update({Alert.loc:loc, Alert.country:country}, synchronize_session = False)
				db.session.commit()
		flash('Fix country success','success')
	except:
		flash('Free usage of ipinfo.io API is limited to 50,000 API requests per month','success')
		pass
	
	return redirect(url_for('alert.report'))