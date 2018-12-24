# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:53:13 2018

@author: gehui
"""

#def get_formatted_name(first, last):
#    """Generate a neatly formatted full name."""
#    full_name = first + ' ' + last
#    return full_name.title()


#def get_formatted_name(first, middle,last):
#    """Generate a neatly formatted full name."""
#    full_name = first + ' ' +middle+' '+ last
#    return full_name.title()

def get_formatted_name(first,last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
