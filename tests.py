from index import app,db
import unittest
from flask_testing import TestCase
class MyTest(TestCase):


    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_port(self):
        port = self.client.get('/')
        print port.data
        assert 'Port Working' in port.data

if __name__ == '__main__':
    unittest.main()