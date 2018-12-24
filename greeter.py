# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:59:58 2018

@author: gehui
"""

#name = input('Please enter your name: ')
#print("Hello, " + name + "!")


#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print("\nHello, " + name + "!")

#def greet_user():
#    """显示简单的问候语"""
#    print("Hello!")
#greet_user()

#def greet_user(user_name):
#    """显示简单的问候语"""
#    print("Hello "+user_name.title()+"!")
#greet_user('ge hui')

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")