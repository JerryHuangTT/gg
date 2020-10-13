from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from gevent import pywsgi
from web_backend import user_get

class Cuser(Resource):
    def get(self, para):
        #body = request.json
        return {'para': para,'body':user_get(para)}

    def put(self, para):
        body = request.json
        return {'para': para,'body':body}

class Cdevice(Resource):
    def get(self, para):
        body = request.json
        return {'para': para,'body':body}

    def put(self, para):
        body = request.json
        return {'para': para,'body':body}

def main():
    app = Flask('jerry')
    api = Api(app)
    api.add_resource(Cuser, '/user/<string:para>')
    api.add_resource(Cdevice, '/device/<string:para>')
    CORS(app, supports_credentials=True)
    server = pywsgi.WSGIServer(('0.0.0.0', 8001), app)
    server.serve_forever()