from app import app
from flask import json

@app.errorhandler(404)
def bad_request(error):
    response = json.dumps(dict(error = 'invalidInput',
    	                       message = 'error'))
    return response, 404