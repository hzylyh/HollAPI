# -*- coding:utf-8 -*-
# author: John Holl

from flask import Flask
import flask_restful as restful

from api.resources.demo1 import Demo1

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Demo1, '/Demo1', '/Demo1/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)