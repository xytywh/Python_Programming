# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:55:18 2018

@author: gehui
"""

#user_0 = {
#          'user_name':'efermi',
#          'first':'enrico',
#          'last':'fermi',
#          }
#print(user_0)
#for key,value in user_0.items():
#    print('\nkey:'+key)
#    print('value:'+value)
    
    
#favorite_languages = {
#                      'jen':'python',
#                      'sarah':'c',
#                      'edward':'ruby',
#                      'phil':'python',
#                      }
#for name in favorite_languages.keys():
#    print(name.title())
    


favorite_languages = {
                      'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python',
                      }
friends = ['jen','phil']
for name in favorite_languages.keys():
    if name in friends:
        print(name+',I know your favorite languages is '+favorite_languages[name])

