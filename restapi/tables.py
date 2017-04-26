from app import db
from flask import json
# TABLE
class Profile(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String, unique = True)
	age = db.Column(db.Integer)
	email = db.Column(db.String, unique = True)

	def __init__(self, username, age, email):
		self.username = username
		self.age = age
		self.email = email

	def __repr__(self):
		return json.dumps(dict(user= self.username, 
							   age= self.age, 
							   email= self.email))

