from tables import Profile
from app import app,db
from flask import request, json
from exceptionsHandler import bad_request

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
	return json.dumps(dict(user = user_id.id))

# REMOVE ------------------------------------------------------------------------------------------------------------

@app.route('/remove/<name>', methods = ['DELETE'])
def remove(name):
	if name:
		dbdelete =  Profile.query.filter_by(username = name).first()
		user_id = dbdelete.id
		db.session.delete(dbdelete)
		db.session.commit()
		return json.dumps(dict(user = user_id))
	else:
		raise bad_request(error)


# UPDATE ------------------------------------------------------------------------------------------------------------

@app.route('/update/<name>', methods = ['PUT'])
def update(name):
	dbupdate = Profile.query.filter_by(username = name).first()
	data = request.get_json()
	dbupdate.username = data['username']
	dbupdate.age = data['age']
	dbupdate.email = data['email']
	db.session.commit()
	return 'User Updated'

# READ ------------------------------------------------------------------------------------------------------------

@app.route('/read', defaults = {'name': None})
@app.route('/read/<name>')
def read(name):
	if name:
		dbread = Profile.query.filter_by(username = name).first()
		return json.dumps(dict(email = dbread.email,
			    	   		   username = dbread.username,
			    	   		   age= dbread.age))
	else:
		dbreadall = Profile.query.all()
		if len(dbreadall) > 0:
			return str(dbreadall)
		else:
			return 'Theres no List'	