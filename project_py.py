# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:20:16 2020

@author: Sara
"""
import pandas as pd

Data = pd.read_excel (r'C:/Users/Sara/Downloads/bigData/Data.xlsx' , header= None )
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
    for i in range (8,20):
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
    for i in range (0, len(listOflist)-1):
        for k in range (i+1, len(listOflist)):
            for j in range (0,level):
                check = True
                sub_list = []
                for l in range (0,level):    
                    sub_list.append(listOflist[i][l])   
                for x in sub_list:
                    if ((x.name == listOflist[k][j].name) 
                    and(x.value == listOflist[k][j].value) ):
                        check =False
                if check == True :
                    sub_list.append(listOflist[k][j])
                    new_listOflist.append(sub_list)
                    
                
                        
    return(new_listOflist)                    
                
            
       ##################################################3
       
attr_values = []
attr_values = Get_atrr_Value()

#for obj in attr_values: 
 #   print( obj.name, obj.value, sep =' ' ) 

obj_list = []

obj_list.append(atrr(8 ,4))

listOfListsOfAtt = []

sublist = []
sublist.append(atrr(6 ,4))
sublist.append(atrr(7 ,1)) 
listOfListsOfAtt.append(sublist)
sublist2 = []
sublist2.append(atrr(6 ,5))
sublist2.append(atrr(8 ,4))    
listOfListsOfAtt.append(sublist2)
sublist3 = []
sublist3.append(atrr(8 ,4))
sublist3.append(atrr(7 ,0))
listOfListsOfAtt.append(sublist3)



listofList = Calculate_Support (listOfListsOfAtt , 2 , 0 )
new_listofList = []
new_listofList = item_Set(listofList , 2 )


for obj in listofList:
    for i in range (0,2):
        print( obj[i].name, obj[i].value, sep =' ' ) 

print(",,,,,,,,")
print(len(new_listofList))

for obj in new_listofList:
    for i in range (0,3):
        print( obj[i].name, obj[i].value, sep =' ' ) 
    
    
    
#print(calculate_min_Support(sublist , 2 , 5))