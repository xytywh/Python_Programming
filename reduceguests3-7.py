# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:37:28 2018

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
print('Sorry,I can only invite two people.')
print('Sorry,'+guests.pop()+",I can't invite you to dinner!")
print('Sorry,'+guests.pop()+",I can't invite you to dinner!")
print('Sorry,'+guests.pop()+",I can't invite you to dinner!")
print('Sorry,'+guests.pop()+",I can't invite you to dinner!")
print(len(guests))
print(guests[0]+',you still in the invited list.')
print(guests[1]+',you still in the invited list.')
del guests[0]
del guests[0]
print(guests)