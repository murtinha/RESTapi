
class BaseConfig(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'


class TestConfig (BaseConfig):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'