# -*- coding:utf-8 -*-
# author: John Holl

from requests import put, get

print(get('http://localhost:5000/todos/5').json())
# print(put('http://localhost:5000/todo2', data={'data': 'Remeber the milk2'}).json())
#
# print(get('http://localhost:5000/todo1').json())

# print(get('http://localhost:5000/todo2').json())