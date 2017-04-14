from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app) 

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
		return '<User %r>' % self.username


# To initialize db - python shell ( from application import db -> db.create_all())

# CRUD

# SERVER TEST

@app.route('/')
def test_port():
	return 'Port Working'

#CREATE

@app.route('/create', methods = ['POST'])
def create():
	username = request.form['username']
	age = request.form['age']
	email = request.form['email']

	dbcreate = Profile(username, age, email)
	db.session.add(dbcreate)
	db.session.commit()
	print 'User added'
	return 'Added   '

# REMOVE

@app.route('/remove' , methods = ['DELETE'], defaults = {'name':None})
@app.route('/remove/<name>', methods = ['DELETE'])
def remove(name):
	if name:
		dbdelete =  Profile.query.filter_by(username = request.form['username']).first()
		db.session.delete(dbdelete)
		db.session.commit()
		print 'User Deleted'
		return 'User Deleted  '
	else:
		db.session.query(Profile).delete()
		db.session.commit()
		print 'List Deleted'
		return 'List Deleted  '	
# UPDATE

@app.route('/update/<name>', methods = ['PUT'])
def update(name):
	dbupdate = Profile.query.filter_by(username = name).first()
	dbupdate.username = request.form['username']
	dbupdate.age = request.form['age']
	dbupdate.email = request.form['email']
	db.session.commit()
	print 'User Updated'
	return 'Updated    '

# READ

@app.route('/read', defaults = {'name': None})
@app.route('/read/<name>')
def read(name):
	if name:
		dbread = Profile.query.filter_by(username = name).first()
		print 'Username %s, Age %d, Email %s' % (dbread.username, dbread.age, dbread.email)
		return 'Username %s, Age %d, Email %s   ' % (dbread.username, dbread.age, dbread.email)
	else:
		dbreadall = Profile.query.all()
		print dbreadall
		return 'All List   '