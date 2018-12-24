# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:45:27 2018

@author: gehui
"""

banned_users = ['andrew','carlina','david']
user = 'marie'

if user not in banned_users:
    print(user.title()+',you can post a reponse if you wish.')
    