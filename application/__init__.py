from flask import Flask
from flask_sqlalchemy import SQLAlchemy

wabapp = Flask(__name__)
wabapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
wabapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(wabapp)

import application.routes