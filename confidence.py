# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:28:40 2020

@author: Hadeel
"""
import pandas as pd
import numpy as np

class atrr:
  def __init__(self, name, value):
    self.name = name
    self.value = value
    
class itemsets_confidence:
  def __init__(self, ListOfAttr, c_value):
    self.ListOfAttr = ListOfAttr
    self.c_value = c_value    
    
Attr_Names = ['MGODGE' , 'MRELGE' , 'MRELSA', 'MRELOV',
              'MFALLEEN', 'MFGEKIND', 'MFWEKIND', 'MOPLHOOG',
              'MOPLMIDD', 'MOPLLAAG', 'MBERHOOG', 'MBERZELF']
 
Data = pd.read_excel ('data.xlsx' , header= None )

def calculate_Support(obj_list , level ,min_support):
    return True 

def Calculate_Confidence(ListOfListOfAttr, min_c):
    i = 0
    ListOfConfidence =[]
    ListOf2attr = []
    length = len(ListOfListOfAttr[0])
    
    for List in ListOfListOfAttr:
        sub = List[:-1]
        ListOf2attr.append(sub)
    
    
    #Calculate Support of rules
    #ListOfall_s = [ 800, 600, 400, 650,350 ]    #For Test
    #ListOfsub_s = [1000, 1000, 1000, 1000, 1000] #For Test
    ListOfall_s = calculate_Support(ListOfListOfAttr, length)
    ListOfsub_s = calculate_Support(ListOf2attr, length-1)
    s1List = np.array(ListOfall_s)
    s2List = np.array(ListOfsub_s)
    all_conf = s1List/s2List
    
    for List in ListOfListOfAttr:
        #s1 = listofsupports[i] ###### For Test
        #s1 = calculate_Support(List, length, min_s)
        #sub = List[:-1]
        #s2 = 1000 ###### For Test
        #s2 = calculate_Support(sub, length-1, min_s)
        if all_conf[i] >= min_c:
            #c = itemsets_confidence(List, all_conf[i])
            ListOfConfidence.append(List)
        i+=1 ###### For Test
        
    return ListOfConfidence 


def Check_Min_Confindence(ListOfListOfAttrWithConf, min_conf): 
    ListOfRules = []
    for item in ListOfListOfAttrWithConf: 
        if item.c_value >= min_conf: 
            ListOfRules.append(item.ListOfAttr)
            
    return ListOfRules

def Convert_to_name (ListOfRules):
    complete_rule = ''
    ListOfRules_named = []
    for List in ListOfRules:
        i = 0
        length = len(List)
        for attr in List: 
            name = Attr_Names[attr.name-1]
            if i == length - 1: ### RIGHT HAND SIDE OF RULE
                complete_rule += ' ===> ' + '(' + name + "," + str(attr.value) + ')' 
                i += 1       
            elif i < length- 1: ### LEFT HAND SIDE OF RULE
                complete_rule += '(' + name + "," + str(attr.value) + ')' 
                i += 1
            
            if i < length-1 : 
                complete_rule += ' , '
        ListOfRules_named.append(complete_rule)
        complete_rule = ''
    return ListOfRules_named


################################ TEST FUNCTIONS #############################

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

min_s = 0.30
min_c = 0.50
listofsupports = [ 800, 600, 400, 650,350 ]    

ListOfRules = Calculate_Confidence(ListOfListOfAttr, min_c)
#ListOfRules = Check_Min_Confindence(ListOfConfidence, min_c)
ListOfRules_named = Convert_to_name(ListOfRules)
for item in ListOfRules_named:
    print(item) 
       
       
       
       
       