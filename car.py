# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:27:02 2018

@author: gehui
"""

#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self, make, model, year):
#        """初始化描述汽车的属性"""
#        self.make = make
#        self.model = model
#        self.year = year
#    def get_descriptive_name(self):
#        """返回整洁的描述性信息"""
#        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#        return long_name.title()
#my_new_car = Car('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())


#class Car():
#    def __init__(self, make, model, year):
#        """初始化描述汽车的属性"""
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        """返回整洁的描述性信息"""
#        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#        return long_name.title()
#    def read_odometer(self):
#        """打印一条指出汽车里程的消息"""
#        print("This car has " + str(self.odometer_reading) + " miles on it.")
#        
#my_new_car = Car('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 30
#my_new_car.read_odometer()

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mile):
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,mile):
        self.odometer_reading += mile
        
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 
        
    def get_range(self):
        """打印一条消息， 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)        
        
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
        
#my_new_car = Car('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())
#
#my_new_car.update_odometer(30)
#my_new_car.read_odometer()
#
#my_new_car.increment_odometer(300)
#my_new_car.read_odometer()

