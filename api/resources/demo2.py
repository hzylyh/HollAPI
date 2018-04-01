# -*- coding:utf-8 -*-
# author: John Holl

from flask import request
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('Content-Type', type=str, location='headers')

class Demo2(Resource):
    def post(self):
        args = parser.parse_args()
        if args['Content-Type'] != 'application/json':
            return "ERROR: Content-type should be application/json"
        else:
            json_data = request.get_json()
            print(json_data)
            return json_data