# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import bottle as bt
import os
from os import environ as env
from sys import argv


@bt.get('/') # or @route('/login')
def init():
    return '''<h1>First Heroku App!!!</h1>'''


bottle.run(host='0.0.0.0', port=argv[1])