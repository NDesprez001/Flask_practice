"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap, practice_1, home_content
from login import login_func
from models import db, Persons
# from Long_lad_zipcode import mk_dict, find_info
import requests
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    
    return home_content(app), 200


@app.route('/practicing', methods=['POST', 'GET'])
def my_work():

    if request.method == 'GET':
        return 'You used GET method'

@app.route('/first_page')
def first_page():
    
    return practice_1(app)


@app.route('/second page', methods=['POST', 'GET'])
def hey():
    return "What's up"

# @app.route('/zipcode info', methods=['POST', 'GET'])

# def long_lad():
#     return mk_dict(), find_info()


    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
