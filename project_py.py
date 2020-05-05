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

    
attr_values = []

def Get_atrr_Value(value_list):
    count = 0 
    num = 0
    for i in range (8,20):
        while num < 45 :    
            for x in Data[i]:
                if x == num :
                    count = count + 1
            if count != 0 :
                value_list.append((atrr(i ,num) , count ))
                count = 0
            num = num + 1 
        num =0 
    return (count)            
            
            
        

print(Get_atrr_Value(attr_values))

for obj in attr_values: 
    print( obj[0].name, obj[0].value,obj[1] ,  sep =' ' ) 
















