from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import json
import os
import subprocess

from db_operator import *


app = Flask(__name__)
api = Api(app)
CORS(app)
      

class QueryType1(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        query_result = db_operate_type1(json_data['qid'])
        print query_result
        return json.dumps(query_result)

class QueryType2(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print json_data
        print json_data['qid']
        print json_data['fname']
        print json_data['lname']
        query_result = db_operate_type2(json_data['qid'], json_data['fname'], json_data['lname'])
        print query_result
        return json.dumps(query_result)

class QueryType3(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print json_data['fname']
        print json_data['lname']
        query_result = db_operate_type3(json_data['fname'], json_data['lname'])
        print query_result
        return json.dumps(query_result)

class QueryType4(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print json_data['fname']
        print json_data['lname']
        query_result = db_operate_type4(json_data['fname'], json_data['lname'])
        print query_result
        return json.dumps(query_result)
    

api.add_resource(QueryType1, '/question1')
api.add_resource(QueryType2, '/question2')
api.add_resource(QueryType3, '/question3')
api.add_resource(QueryType4, '/question4')



if __name__ == '__main__':
    app.run(debug=True)
