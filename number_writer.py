# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:17:35 2018

@author: gehui
"""

import json

numbers = [2,3,5,7,11,13]

filename = 'number.json'


with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)