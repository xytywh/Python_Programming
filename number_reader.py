# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:23:07 2018

@author: gehui
"""

import json


filename = 'number.json'


with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)