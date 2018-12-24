# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:10:14 2018

@author: gehui
"""

from car import Car


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.increment_odometer(300)
my_new_car.read_odometer()