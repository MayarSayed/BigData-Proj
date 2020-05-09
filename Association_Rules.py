# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:20:16 2020
@author: Sara
"""
import pandas as pd
import numpy as np

#Data = pd.read_excel (r'E:/Mayar kolya/GitHub repos/BigData-Proj/data.xlsx' , header= None )
#print (Data[8])

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

def Get_atrr_Value():
    #Each attribute with multi values
    attr_values = [] 
#    count = 0 
    num = 0
    for i in range (8,20):
        while num < 10 :    
            for x in Data[i]:
                if x == num :
                    attr_values.append(atrr(i ,num))
                    break
            num = num + 1 
        num =0 
    return (attr_values)    

def Min_Support_list(attr_values , level , min_support ):
    listofList = []
    count_list = []
    
    count_list = Calculate_Support(attr_values , level)
       
    for n in range(0,len(count_list)):
        if (count_list[n]/5822) >= min_support:
            listofList.append(attr_values[n])
        '''
        for i in range ( 0 , len(attr_values)):
            support = calculate_Support(attr_values[i], level , min_support)
            if support >= min_support :
                listofList.append(attr_values[i])
        
        #print(attr_values[i].name)
        if level == 1:
            listofList = cal_Min_sup2(attr_values , level , min_support)
            
            temp_list.append(attr_values[i] )
            support = calculate_Support(temp_list, level , min_support)
            temp_list.clear()
            '''
           
    return (listofList)         
        
'''      
                
def calculate_Support_old(obj_list , level ,min_support):
    row = 0 
    check = True
    count = 0
    
    for i in range (0,100):
        ##############
        check = True
        if Data[obj_list[0].name][i] == obj_list[0].value:
            row = i 
            if level != 1:
                for j in range (1 , level) :
                    if Data[obj_list[j].name][row] != obj_list[j].value:
                        check = False
                if check == True :
                    count = count + 1
            else:
                count = count + 1
    support = count / 1##########
   # if support >= min_support :
    return(support)  
'''
################################    
def Calculate_Support(attr_values , level):
   # listofList = []
    count_list = [0] * len(attr_values)
    for i in range (0,5822):
       # print('5ls row')
        if level == 1:
            for k in range(0,len(attr_values)):
                if Data[attr_values[k].name][i] == attr_values[k].value:
                    count_list[k] = count_list[k]+1
        else:
            for l in range(0,len(attr_values)):
                count =0
                for m in range(0,level):
                    if Data[attr_values[l][m].name][i] ==attr_values[l][m].value:
                        count = count +1
                    else:
                        break
                if count == level:
                    #print(str(l)+ '  '+ str(count_list[l]))
                    count_list[l]= count_list[l]+1
    '''
    for n in range(0,len(count_list)):
        if count_list[n] >= min_support:
            listofList.append(attr_values[n])
    '''
    return(count_list)
##############################
def item_Set(listOflist , level):
    new_listOflist = []
    check = True
    Exist = False
    
    if len(listOflist) == 1:
        return(listOflist,False)
    #i : counter for first list
    for i in range (0, len(listOflist)-1):
        #k: counter for sec list
        for k in range (i+1, len(listOflist)):
            if level == 1:
                sub_list2 = []
                sub_list2.append(listOflist[i])
                sub_list2.append(listOflist[k])
                new_listOflist.append(sub_list2)
                
            else: 
                #j: counter for obj in sec list
                for j in range (0,level):
                    check = True
                    Exist = False
                    sub_list = []
                    #l: counter for obj in first list
                    for l in range (0,level):    
                        sub_list.append(listOflist[i][l])
                    #check if obj is already in sublist or in same col   
                    for x in sub_list:
                        if (x.name == listOflist[k][j].name):
                            check =False
                    if check == True :
                        sub_list.append(listOflist[k][j])
                        #check if sublist already in new_listOflist
                        for m in range(0,len(new_listOflist)):
                            count =0
                            #n: counter for obj in sublist
                            for n in sub_list:
                                #p: counter for obj in new_listOflist
                                for p in new_listOflist[m]:
                                    if ((n.name == p.name) and(n.value == p.value)):
                                        #print('heeeeeereeee')
                                        count = count +1
                            if count == level+1:
                                Exist = True
                        if Exist == False:
                            new_listOflist.append(sub_list)
                    
                
                        
    return(new_listOflist,True)                    
                

def main_fn(att_list, min_support):
    level_no = 1
    new_list = []
    old_list = []
    add = True
    while True:
        #new list after removing min support
       # print("****")
        new_list = Min_Support_list(att_list , level_no , min_support )
       # print(len(new_list))
       # for obj in new_list:
        #    print("****")
            #for i in range (0,level_no):
          #  print( obj.name, obj.value, sep =' ' ) 
        if len(new_list) == 0:
            return(old_list)
        else:
            old_list = new_list
            att_list,add = item_Set(new_list , level_no)
            if add == True:
                #print(level_no)
                #print('************************')
                level_no = level_no +1
            else:
                return(old_list)
             
       ##################################################3
       ###################################################

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
    ListOfall_s = Calculate_Support(ListOfListOfAttr, length)
    ListOfsub_s = Calculate_Support(ListOf2attr, length-1)
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
            name = Attr_Names[attr.name-9]
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

       ###################################################
attr_values = []
attr_values = Get_atrr_Value()
print("----------------- Finished Get atributes Values")
ListOfListOfAttr = main_fn(attr_values, 0.1374)
print("----------------- Finished Get Last Level itemsets")
combinations = Create_rules(ListOfListOfAttr)
print("----------------- Finished Rules combinations")
ListOfRules = Calculate_Confidence(combinations, 0.5)
print("----------------- Finished Get min confidence rules")
ListOfRules_named = Convert_to_name(ListOfRules)

for item in ListOfRules_named:
    print(item) 

