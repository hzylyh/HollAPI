# -*- coding:utf-8 -*-
# author: John Holl

from flask import request
from flask_restful import Resource, reqparse

names = {}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

class Demo1(Resource):
    def get(self, name):
        return "get请求-名字是%s" % name

    def post(self):
        args = parser.parse_args()
        name = request.form['name']
        print(args)
        # todos[todo_id] = {'data': args['data']}
        # return {todo_id: todos[todo_id]}
        return "您的名字是%s" % name