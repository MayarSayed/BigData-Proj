# -*- coding: utf-8 -*-
"""
Created on Fri May  8 05:30:30 2020

@author: Nour
"""
import pandas as pd
import numpy as np

class atrr:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
def Create_rules(ListOfListOfAttr): 
    combinations = []
    for List in ListOfListOfAttr:
        npl = np.array(List)
        Length = len(List)
        i = 0
        while i < Length:
            if i == Length-1: 
                combinations.append(npl)
                i +=1
            elif i < Length-1:
                new_list = [] 
                l_attr = npl[Length-1]
                k_attr = npl[i]
                j = 0
                while j < Length:
                    if j == i:
                        new_list.append(l_attr)
                        j += 1
                    elif j == Length-1 : 
                        new_list.append(k_attr)
                        j += 1
                    else:
                        new_list.append(npl[j])
                        j += 1
                combinations.append(new_list)
                i += 1
    return combinations


ListOfListOfAttr= []

sublist = []
sublist.append(atrr(1 ,1))
sublist.append(atrr(4 ,1))
ListOfListOfAttr.append(sublist)

sublist = []
sublist.append(atrr(2 ,1)) 
sublist.append(atrr(5 ,1)) 
ListOfListOfAttr.append(sublist)

sublist = []
sublist.append(atrr(2 ,1)) 
sublist.append(atrr(4 ,1)) 
ListOfListOfAttr.append(sublist)

sublist = []
sublist.append(atrr(3 ,1)) 
sublist.append(atrr(5 ,1)) 
ListOfListOfAttr.append(sublist)


sublist = []
sublist.append(atrr(3 ,1)) 
sublist.append(atrr(4 ,1))
ListOfListOfAttr.append(sublist)

combinations = Create_rules(ListOfListOfAttr)

for List in combinations:
    for item in List: 
        print(item.name, "," , item.value)
    print("-------------")
