from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app) 

from tables import Profile
import routes
# To initialize db - python shell ( from application import db -> db.create_all())

	