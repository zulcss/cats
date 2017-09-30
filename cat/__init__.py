import os

from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

api_key = os.environ['API_KEY']
URL = "https://thecatapi.com/api/images/get?format=xml&api_key="+ api_key

from cat import views
