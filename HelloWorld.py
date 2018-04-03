# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import bottle as bt


@bt.get('/') # or @route('/login')
def init():
    return '<h1>First Heroku App!!!</h1>'


bt.run(host='localhost', port=80, server='paste')