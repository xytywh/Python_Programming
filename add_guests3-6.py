# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:29:25 2018

@author: gehui
"""

guests = ['Newton','Einstein','Turing']
print(guests[0]+',would you like to have dinner with me!')
print(guests[1]+',would you like to have dinner with me!')
print(guests[2]+',would you like to have dinner with me!')

print('I have just found a bigger dining table!')
guests.insert(0,'Leibniz')
guests.insert(len(guests)//2,'Taylor')
guests.append('Hiton')
print(guests[0]+',would you like to have dinner with me!')
print(guests[1]+',would you like to have dinner with me!')
print(guests[2]+',would you like to have dinner with me!')
print(guests[3]+',would you like to have dinner with me!')
print(guests[4]+',would you like to have dinner with me!')
print(guests[5]+',would you like to have dinner with me!')