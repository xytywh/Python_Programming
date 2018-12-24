# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:26:10 2018

@author: gehui
"""

#unprined_models = ['ao te man','spider man','iron man']
#printed_models =[]
#while unprined_models:
#    printing_model = unprined_models.pop()
#    print('The printing model is '+printing_model+'.')
#    printed_models.append(printing_model)
#
#print('The following models are printed:')
#for printed_model in printed_models:
#    print(printed_model)
    
    
    
 
def printing_models(unprined_models,printed_models):
    while unprined_models:
        printing_model = unprined_models.pop()
        print('The printing model is '+printing_model+'.')
        printed_models.append(printing_model)
        
def show_printed_model(printed_models):
    print('The following models are printed:')
    for printed_model in printed_models:
        print(printed_model)
unprined_models = ['ao te man','spider man','iron man']
printed_models =[]
print(printing_models.__doc__)
print(unprined_models)
printing_models(unprined_models[:],printed_models)
print(unprined_models)
show_printed_model(printed_models)
