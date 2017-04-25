from flask import json,jsonify
from app import app,db
from tables import Profile
import unittest
from flask_testing import TestCase

class BaseTestCase(TestCase):


    def create_app(self):        
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):        
        db.create_all()

    def tearDown(self):        
        db.session.remove()
        db.drop_all()


class MyTest(BaseTestCase):

    def health_check(self):        
        response = self.client.get('/health-check')
        self.assertIn('It works', response.data)
    
# CREATE ------------------------------------------------------------------------------------------------------------

    def test_add_user(self):
        response = self.client.post('/create', data = json.dumps(dict(username='hel',
                                                                     age=24,
                                                                     email='helgod@gamcil.com')),
                                                                     content_type='application/json')
        user= Profile.query.filter_by(username = 'hel').first()
        self.assertEqual(json.dumps(dict(user= 1)), response.data)
        self.assertEqual('hel', user.username)
        self.assertEqual(24, user.age)
        self.assertEqual('helgod@gamcil.com', user.email)
    
# DELETE ------------------------------------------------------------------------------------------------------------

    def test_delete_user(self):
        user1 = Profile('Eric',25,'email@eric.com')
        user2 = Profile('user2',2,'usr2@ff.com')
        db.session.add(user1)
        db.session.commit()
        db.session.add(user2)
        db.session.commit()
        user1query = Profile.query.filter_by(username = "Eric").first()
        user2query = Profile.query.filter_by(username = "user2").first()
        user2_id = user2query.id
        response = self.client.delete('/remove/user2')
        removed_user = Profile.query.filter_by(username = "user2").first()
        self.assertEqual(removed_user, None) # to guarantee that the user was removed from db
        self.assertEqual(json.dumps(dict(user= user2query.id)), response.data)
        self.assertEqual('email@eric.com', user1query.email) # checking if db wasnt erased right after the delete request (as said in flask-testing documentation)
    
# UPDATE ------------------------------------------------------------------------------------------------------------

    def test_update_user(self):
        user = Profile('Marta',22,'marta@mar.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.put('/update/Marta', data=json.dumps(dict(username= 'Karen',
                                                                         age= 15,
                                                                         email= 'karen@ka.com')),
                                                                         content_type='application/json')
        userquery = Profile.query.filter_by(username='Karen').first()
        self.assertEqual('karen@ka.com', userquery.email)

# READ ------------------------------------------------------------------------------------------------------------

    def test_read_users(self):
        user1 = Profile('Paty',30,'paty@li.com')
        db.session.add(user1)
        db.session.commit()
        user2 = Profile('Bel',23,'bec@22.com')
        db.session.add(user2)
        db.session.commit()
        response = self.client.get('/read')
        self.assertIn('Whole List', response.data)

    def test_read_no_users(self):
        response = self.client.get('/read')
        self.assertIn('Theres no List', response.data)

    def test_read_user(self):
        user1 = Profile('user',29,'user@gg.com')
        db.session.add(user1)
        db.session.commit()
        response = self.client.get('read/user')
        self.assertEqual(json.dumps(dict(username= 'user', 
                                         age = 29,
                                         email= 'user@gg.com')),response.data) 

if __name__ == '__main__':
    unittest.main()