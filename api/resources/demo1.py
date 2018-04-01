# -*- coding:utf-8 -*-
# author: John Holl

from flask import request
from flask_restful import Resource, reqparse

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('data', type=int)

class Demo1(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        # args = parser.parse_args()
        # todos[todo_id] = request.form['data']
        # print(args)
        # todos[todo_id] = {'data': args['data']}
        # return {todo_id: todos[todo_id]}
        return "bbb"