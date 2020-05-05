# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:08:53 2020

@author: Mayar Sayed
"""

# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("E:/Mayar kolya/Big Data/Project/data.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(2, 8)) 

noOfAttributes =5
noOfCol = 3
#define attribute class
class Attribute:
  def __init__(self, col , value):
    self.col = col
    self.value = value
    
listOfListsOfAtt = []
for i in range(0,2):
    sublist = []
    for j in range(0,10)
        sublist.append((i,j))
    listoflists.append(sublist)
print listoflists
    
#itterate on Excell sheet 
#create obj of Attribute and add to list of list of attributes
for i in range(noOfCol):
    for j in range(noOfAttributes):
        attObj = Attribute(i,sheet.cell_value(j, i))
        #attObj2 = Attribute(i,sheet.cell_value(1, 1))
        listOfListsOfAtt.append((attObj))
        #print(i)
        #print(j)
print(listOfListsOfAtt[0])


