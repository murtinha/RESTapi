from flask import json
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
    
    def test_add_user(self):
        post = self.client.post('/create', data = json.dumps(dict(username='hel',age=24,email='helgod@gamcil.com')),content_type='application/json')
        assert 'Added   ' in post.data
    
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
    # def test_update_user(self):
    #     user = Profile("Maria",12,"maria@ddcom")
    #     db.session.add(user)
    #     db.session.commit()
    #     updateUser = Profile.query.filter_by(username = "Maria").first()
    #     updateUser.username = "Carla"
    #     assert "Carla" in user.username 
    # def test_read_user(self):

if __name__ == '__main__':
    unittest.main()