#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv
import bottle as bt
import pandas as pd
import numpy as np

@bt.get('/') # or @route('/login')
def init():
	
    return bt.static_file("index.html",root="files/") 


bt.run(host='0.0.0.0', port=argv[1])