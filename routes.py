from tables import Profile
from app import app,db
from flask import jsonify, request
# CRUD

# SERVER TEST

@app.route('/health-check')
def health_check():
	return 'It works'

#CREATE ------------------------------------------------------------------------------------------------------------

@app.route('/create', methods = ['POST'])
def create():
	data = request.get_json()
	username = data['username']
	age = data['age']
	email = data['email']

	dbcreate = Profile(username, age, email)
	db.session.add(dbcreate)
	db.session.commit()
	user_id = Profile.query.filter_by(username = username).first()
	print 'User added'
	return 'User created with id = %d' % user_id.id

# REMOVE ------------------------------------------------------------------------------------------------------------

@app.route('/remove' , methods = ['DELETE'], defaults = {'name':None})
@app.route('/remove/<name>', methods = ['DELETE'])
def remove(name):
	if name:
		dbdelete =  Profile.query.filter_by(username = name).first()
		user_id = dbdelete.id
		db.session.delete(dbdelete)
		db.session.commit()
		print 'User Deleted'
		return 'User with id %d deleted' % user_id
	else:
		print 'Input name'
		return 'Input name'	

# UPDATE ------------------------------------------------------------------------------------------------------------

@app.route('/update/<name>', methods = ['PUT'])
def update(name):
	dbupdate = Profile.query.filter_by(username = name).first()
	dbupdate.username = request.form['username']
	dbupdate.age = request.form['age']
	dbupdate.email = request.form['email']
	db.session.commit()
	print 'User Updated'
	return 'User Updated'

# READ ------------------------------------------------------------------------------------------------------------

@app.route('/read', defaults = {'name': None})
@app.route('/read/<name>')
def read(name):
	if name:
		dbread = Profile.query.filter_by(username = name).first()
		print 'Username %s, Age %d, Email %s' % (dbread.username, dbread.age, dbread.email)
		return jsonify(email = dbread.email,
			    	   username = dbread.username,
			    	   age= dbread.age  )
	else:
		dbreadall = Profile.query.all()
		if len(dbreadall) > 0:
			print dbreadall
			return 'Whole List' # didnt manage to return the columns
		else:
			print 'Theres no List'
			return 'Theres no List'	