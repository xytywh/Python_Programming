# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:15:56 2018

@author: gehui
"""


filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))


#filename = 'pi_million_digits.txt'
#with open(filename) as file_object:
#    lines = file_object.readlines()
#pi_string = ''
#for line in lines:
#    pi_string += line.strip()
#    print(pi_string[:52] + "...")
#print(len(pi_string))