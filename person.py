# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:14:00 2018

@author: gehui
"""


#def build_person(first_name, last_name):
#    """返回一个字典， 其中包含有关一个人的信息"""
#    person = {'first': first_name, 'last': last_name}
#    return person
#musician = build_person('jimi', 'hendrix')
#print(musician)

def build_person(first_name, last_name, age=''):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)