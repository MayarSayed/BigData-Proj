# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:20:16 2020

@author: Sara
"""
import pandas as pd

Data = pd.read_excel (r'E:/Mayar kolya/GitHub repos/BigData-Proj/data.xlsx' , header= None )
#print (Data[8])

class atrr:
  def __init__(self, name, value):
    self.name = name
    self.value = value


def Get_atrr_Value():
    #Each attribute with multi values
    attr_values = [] 
    count = 0 
    num = 0
    for i in range (9,12):
        while num < 45 :    
            for x in Data[i]:
                if x == num :
                    count = count + 1
            if count != 0 :
                attr_values.append(atrr(i ,num))
                count = 0
            num = num + 1 
        num =0 
    return (attr_values)    

def Calculate_Support(attr_values , level , min_support ):
    check = True
    listofList = []
    temp_list = []
    for i in range ( 0 , len(attr_values)):
        
        #print(attr_values[i].name)
        if level == 1:
            temp_list.append(attr_values[i] )
            check = calculate_min_Support(temp_list, level , min_support)
            temp_list.clear()
        else :
            check = calculate_min_Support(attr_values[i], level , min_support)
        if check == True :
            listofList.append(attr_values[i])
    return (listofList)         
        
        
                
def calculate_min_Support(obj_list , level ,min_support):
    row = 0 
    check = True
    count = 0 
    for i in range (0,20):
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
    if support >= min_support :
        return(True)  
    else : 
        return(False)
    
  
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
                    #check if obj is already in sublist    
                    for x in sub_list:
                        if ((x.name == listOflist[k][j].name) 
                        and(x.value == listOflist[k][j].value) ):
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
        new_list = Calculate_Support(att_list , level_no , min_support )
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
                level_no = level_no +1
            else:
                return(old_list)
             
       ##################################################3
       
attr_values = []
attr_values = Get_atrr_Value()
#new_list = Calculate_Support(attr_values , 1 , 2 )
list4 = main_fn(attr_values, 2)
print(len(list4))
#for obj in list4: 
  #  for i in range(0,5):
   #     print( obj[i].name, obj[i].value, sep =' ' ) 
'''
obj_list = []

obj_list.append(atrr(8 ,4))

listOfListsOfAtt = []

sublist = []
sublist.append(atrr(9 ,0))
sublist.append(atrr(9,1))
sublist.append(atrr(9 ,2)) 
listOfListsOfAtt.append(sublist)
sublist2 = []
sublist2.append(atrr(6 ,5))
sublist2.append(atrr(8 ,4))    
listOfListsOfAtt.append(sublist2)
sublist3 = []
sublist3.append(atrr(8 ,4))
sublist3.append(atrr(7 ,0))
listOfListsOfAtt.append(sublist3)
sublist4 = []
sublist4.append(atrr(6 ,5))
sublist4.append(atrr(7 ,0))
listOfListsOfAtt.append(sublist4)



#listofList = Calculate_Support (sublist , 1 , 0 )
#new_listofList = []
#new_listofList = item_Set(listofList , 0)


for obj in listofList:
   # for i in range (0,2):
   print( obj.name, obj.value, sep =' ' ) 

print(",,,,,,,,")

#print(len(list4))

#for obj in new_listofList:
 #   print("****")
  #  for i in range (0,3):
   #     print( obj[i].name, obj[i].value, sep =' ' ) 
    
    
    
print(calculate_min_Support(sublist , 2 , 5))
'''