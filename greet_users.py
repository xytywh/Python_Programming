# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:21:42 2018

@author: gehui
"""

def greet_users(user_lists):
    for user in user_lists:
        print('Hello '+user.title()+'!')


user_lists = ['ge hui','jiang wen jie','shi peng fei']
greet_users(user_lists)