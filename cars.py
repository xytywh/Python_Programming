# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:46:08 2018

@author: gehui
"""

#cars = ['bmw','audi','toyota','subaru']
#cars.sort()
#print(cars)
#
#
#cars = ['bmw','audi','toyota','subaru']
#cars.sort(reverse=True)
#print(cars)


#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print('Here is the original list:')
#print(cars)
#print('\nHere is the sorted list:')
#print(sorted(cars))
#print('Here is the original list again:')
#print(cars)



#cars = ['bmw', 'audi', 'toyota', 'subaru']
#print(cars)
#cars.reverse()
#print(cars)
#print(len(cars))


cars = ['audi','bmw',  'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())