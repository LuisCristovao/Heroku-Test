#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv
import bottle as bt
import pandas as pd
import numpy as np

counter=0

@bt.get('/') # or @route('/login')
def init():
    global counter
    counter+=1
    #return "<h1>First Heroku App "+str(np.random.random_sample())+" !!!</h1>"
    return "<h1>Your are the visitor "+str(counter)+" !!!</h1>"


bt.run(host='0.0.0.0', port=argv[1])