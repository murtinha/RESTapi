from app import db

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
		return 'Id: %d, User: %s, Age: %d, Email: %s>' % (self.id,self.username,self.age,self.email)

