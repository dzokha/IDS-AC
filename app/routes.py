import os
import sys
import json
import shutil
from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for, send_from_directory
# from flask_login import login_user, logout_user, current_user, login_required



from flask import Flask, request, jsonify
# app = Flask(__name__)
template_dir = os.path.abspath('ac/views')

# Blueprint
routes = Blueprint('home', __name__, template_folder=template_dir)



# Home page
@routes.route('/')
def index():
    return render_template('layout/home.html', title='IDS-AC')

# Extraction tcpfeature page
@routes.route('/extraction')
def extraction():
    return render_template('layout/extraction.html', title='Extraction tcpfeature')

# Network monitoring page
@routes.route('/monitoring')
def monitoring():
    return render_template('layout/monitoring.html', title='Network monitoring')













# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from url parameter
#     name = request.args.get("name", None)

#     # For debugging
#     print(f"got name {name}")

#     response = {}

#     # Check if user sent a name at all
#     if not name:
#         response["ERROR"] = "no name found, please send a name."
#     # Check if the user entered a number not a name
#     elif str(name).isdigit():
#         response["ERROR"] = "name can't be numeric."
#     # Now the user entered a valid name
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

#     # Return the response in json format
#     return jsonify(response)

# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {name} to our awesome platform!!",
#             # Add this option to distinct the POST request
#             "METHOD" : "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "no name found, please send a name."
#         })

