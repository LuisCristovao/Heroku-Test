#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv
import bottle as bt


@bt.get('/') # or @route('/login')
def init():
    return '''<h1>First Heroku App2!!!</h1>'''


bt.run(host='0.0.0.0', port=argv[1])