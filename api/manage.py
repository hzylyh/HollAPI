# -*- coding:utf-8 -*-
# author: John Holl

from flask import Flask
import flask_restful as restful

from api.resources.demo1 import Demo1
from api.resources.demo2 import Demo2

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Demo1, '/Demo1', '/Demo1/<string:name>')
api.add_resource(Demo2, '/Demo2')

if __name__ == '__main__':
    app.run(debug=True)