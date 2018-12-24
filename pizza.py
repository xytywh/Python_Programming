# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:41:10 2018

@author: gehui
"""


# pizza = {
#         'crust':'thick',
#         'toppings':['mushrooms','extra cheese'],
#         }
#         
#         
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
# "with the following toppings:")
# for topping in pizza['toppings']:
#    print("\t" + topping)


# def make_pizza(*toppings):
#    print(toppings)
#    
#    
# make_pizza('mushrooms','green peppers')
# make_pizza('pepperoni')


# def make_pizza(*toppings):
#    print('\nMaking a pizza with the following toppings:')
#    for topping in toppings:
#        print('-'+topping)
#    
# make_pizza('mushrooms','green peppers')
# make_pizza('pepperoni')

def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)


#
# make_pizza(13,'mushrooms','green peppers')
# make_pizza(11,'pepperoni')


# def build_profile(first,last,**user_info):
#    profile = {}
#    profile['first name'] = first
#    profile['last name'] = last
#    for key,value in user_info.items():
#        profile[key] = value
#    print(profile)
#    
# build_profile('ge','hui',xueli = 'graduate',age = '25')

make_pizza(10,'mushrooms')
