# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:35:40 2018

@author: gehui
"""

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")