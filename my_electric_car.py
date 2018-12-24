# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:13:55 2018

@author: gehui
"""

from car import ElectricCar


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
