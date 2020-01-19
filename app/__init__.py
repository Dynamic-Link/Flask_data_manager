from flask import Flask, jsonify, request
from decouple import config
from flask_pymongo import PyMongo
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)
    ACCESS_KEY = config('ACCESS_KEY')
    CORS(app)


    @app.route(f"/{ACCESS_KEY}/insert_links", methods = ['POST'])
    def insert():
        data = request.get_json(force=True)
        doc = mongo.db.direct_logic.insert(data)
        return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/get_links", methods = ['GET'])
    def getdata():
        data = request.args.get('id')
        doc = mongo.db.direct_logic.find_one({'_id':data})
        return jsonify(doc)

    return app
