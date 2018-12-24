# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:25:33 2018

@author: gehui
"""

import json


username = input("What's your name?")

filename = 'username.json'

with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print('Welcome you,'+username.title())