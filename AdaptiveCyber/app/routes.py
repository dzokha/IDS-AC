import os
import sys
import json
import shutil
from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for, send_from_directory



from flask import Flask, request, jsonify
# app = Flask(__name__)
template_dir = os.path.abspath('app/views')

# Blueprint
routes = Blueprint('home', __name__, template_folder=template_dir)


# Home page
@routes.route('/')
def index():
    return render_template('layout/home.html', title='tcpfeature')