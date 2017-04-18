from flask import json,jsonify
from index import app,db,Profile
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

    def test_port(self):        
        port = self.client.get('/')
        assert 'Port Working' in port.data
    
# CREATE ------------------------------------------------------------------------------------------------------------

    def test_add_user(self):
        post = self.client.post('/create', data = json.dumps(dict(username='hel',
                                                                  age=24,
                                                                  email='helgod@gamcil.com')),
                                                                  content_type='application/json')
        assert 'Added   ' in post.data
    
# DELETE ------------------------------------------------------------------------------------------------------------

    def test_delete_user(self):
        user1 = Profile('Eric',25,'email@eric.com')
        user2 = Profile('user2',2,'usr2@ff.com')
        db.session.add(user1)
        db.session.commit()
        db.session.add(user2)
        db.session.commit()
        user2query = Profile.query.filter_by(username = "user2").first()
        delete = self.client.delete('/remove/Eric', data = {'username':'Eric'})
        assert 'User Deleted'
        assert 'usr2@ff.com' in user2query.email # checking if db wasnt erased right after the delete request (as said in flask-testing documentation)
    
# UPDATE ------------------------------------------------------------------------------------------------------------

    def test_update_user(self):
        user = Profile('Marta',22,'marta@mar.com')
        db.session.add(user)
        db.session.commit()
        update = self.client.put('/update/Marta', data={'username':'Karen',
                                                        'age':15,
                                                        'email':'karen@ka.com'})
        userquery = Profile.query.filter_by(username='Karen').first()
        assert 'karen@ka.com' in userquery.email

# READ ------------------------------------------------------------------------------------------------------------

    def test_read_users(self):
        user1 = Profile('Paty',30,'paty@li.com')
        db.session.add(user1)
        db.session.commit()
        user2 = Profile('Bel',23,'bec@22.com')
        db.session.add(user2)
        db.session.commit()
        read = self.client.get('/read')
        assert "Whole List" in read.data


if __name__ == '__main__':
    unittest.main()