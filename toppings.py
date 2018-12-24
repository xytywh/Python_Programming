# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:57:41 2018

@author: gehui
"""

requested_toppings=['mushrooms','extra cheese']

#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni.")
#    
#print("\nFinished making your pizza!")




#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#elif 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")
#elif 'pepperoni' in requested_toppings:
#    print("Adding pepperoni.")
#    
#print("\nFinished making your pizza!")



#requested_toppings=['mushrooms','extra cheese','green peppers']
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("Sorry,we are out of green peppers right now.")
#    else:
#        print("Adding "+requested_topping+'.')
#    
#print("\nFinished making your pizza!")



#requested_toppings = []
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print("Adding "+requested_topping+'.')
#    print("\nFinished making your pizza!")
#else:
#    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple'
                      ,'extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+'.')
    else:
        print("Srorry,we don't have "+requested_topping+'.')
print("\nFinished making your pizza!")
    