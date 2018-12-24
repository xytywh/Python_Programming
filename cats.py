# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:29:57 2018

@author: gehui
"""

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)