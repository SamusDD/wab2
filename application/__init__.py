from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

wabapp = Flask(__name__)
wabapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
wabapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
wabapp.config['SECRET_KEY'] = getenv('secret_key')


db = SQLAlchemy(wabapp)

import application.routes