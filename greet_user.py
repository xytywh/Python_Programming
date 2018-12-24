# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:29:57 2018

@author: gehui
"""

import json



filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print('Welcome you,'+username.title())