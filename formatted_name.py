# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:07:37 2018

@author: gehui
"""


#def get_formatted_name(first_name, last_name):
#    """返回整洁的姓名"""
#    full_name = first_name + ' ' + last_name
#    return full_name.title()
#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)
#print(get_formatted_name('jimi', 'hendrix'))


#def get_formatted_name(first_name, middle_name, last_name):
#    """返回整洁的姓名"""
#    full_name = first_name + ' ' + middle_name + ' ' + last_name
#    return full_name.title()
#musician = get_formatted_name('john', 'lee', 'hooker')
#print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)