#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv
import bottle
from bottle import default_app, request, route, response, get

@get('/') # or @route('/login')
def init():
    return '''<h1>First Heroku App!!!</h1>'''


bottle.run(host='0.0.0.0', port=argv[1])