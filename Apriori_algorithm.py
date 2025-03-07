import pandas as pd
import numpy as np

#imoporting DataSet from eceel sheet
Data = pd.read_excel (r'E:/Mayar kolya/GitHub repos/BigData-Proj/data.xlsx' , header= None )

#Class attr: to save each attribute name and value
class atrr:
  def __init__(self, name, value):
    self.name = name
    self.value = value
    
#Calss itemsets_confidence : to save the confidence for List of attributes
class itemsets_confidence:
  def __init__(self, ListOfAttr, c_value):
    self.ListOfAttr = ListOfAttr
    self.c_value = c_value   

#List of name of 12 attributes from (col8 : col20)    
Attr_Names = ['MGODGE' , 'MRELGE' , 'MRELSA', 'MRELOV',
              'MFALLEEN', 'MFGEKIND', 'MFWEKIND', 'MOPLHOOG',
              'MOPLMIDD', 'MOPLLAAG', 'MBERHOOG', 'MBERZELF']
###########################################################################################
#Function Get_atrr_Value : Returns List of name and value of attributes from (col8 : col20) "12attribute" 
def Get_atrr_Value():
    #Each attribute with multi values
    attr_values = [] 
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
###########################################################################################
#function Min_Support_list : Returns List of List of attribute name and value for only
#those attributes which count more than or equal to min support and the others are pruned
def Min_Support_list(attr_values , level , min_support ):
    listofList = []
    count_list = []
    
    count_list = Calculate_Support(attr_values , level)
       
    for n in range(0,len(count_list)):
        if (count_list[n]/5822) >= min_support:
            listofList.append(attr_values[n])
              
    return (listofList)         
###########################################################################################        
#function Calculate_Support :  Returns the count of each attribute in List            
def Calculate_Support(attr_values , level):
    count_list = [0] * len(attr_values)
    for i in range (0,5822):
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
                    count_list[l]= count_list[l]+1
    return(count_list)            
###########################################################################################
#Function item_Set : Returns k+1-itemset by joining k-itemset with itself            
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
                                        count = count +1
                            if count == level+1:
                                Exist = True
                        if Exist == False:
                            new_listOflist.append(sub_list)
    return(new_listOflist,True)            
###########################################################################################    
#function main_fn ; Returns Final List when the most frequent itemset is achieved    
def main_fn(att_list, min_support):
    level_no = 1
    new_list = []
    old_list = []
    add = True
    while True:
        #new list after removing min support
        new_list = Min_Support_list(att_list , level_no , min_support )
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
 ###########################################################################################   
#Function Calculate_Confidence : Returns 
def Calculate_Confidence(ListOfListOfAttr, min_c):
    i = 0
    ListOfConfidence =[]
    ListOfLHS = []
    ListOfRHS = []
    length = len(ListOfListOfAttr[0])
    
    for List in ListOfListOfAttr:
        sub = List[:-1]
        ListOfLHS.append(sub)
        ListOfRHS.append(List[-1])
    
    #Calculate Support of rules
    ListOfall_s = Calculate_Support(ListOfListOfAttr, length)
    ListOfsub_s = Calculate_Support(ListOfLHS, length-1)
    s1List = (np.array(ListOfall_s))/5822
    s2List = (np.array(ListOfsub_s))/5822
    all_conf = s1List/s2List
    
    for List in ListOfListOfAttr:
        if all_conf[i] >= min_c:
            ListOfConfidence.append(List)
        i+=1 ###### For Test
        
    return (ListOfLHS ,ListOfRHS, ListOfConfidence)
###########################################################################################
#function Check_Min_Confindence : Returns 
def Check_Min_Confindence(ListOfListOfAttrWithConf, min_conf): 
    ListOfRules = []
    for item in ListOfListOfAttrWithConf: 
        if item.c_value >= min_conf: 
            ListOfRules.append(item.ListOfAttr)
            
    return ListOfRules
###########################################################################################
#fnction Convert_to_name:Returns each attribute it's Name
def Convert_to_name (ListOfRules): 
    RHS = ''
    LHS = ''
    ListOfRules_named = []
    for List in ListOfRules:
        i = 0
        length = len(List)
        for attr in List: 
            name = Attr_Names[attr.name-8]
            if i == 0: ### LEFT HAND SIDE OF RULE
                LHS += '(' + name + "_" + str(attr.value) 
                i += 1
            elif i == length - 1: ### RIGHT HAND SIDE OF RULE
                RHS += '(' + name + "_" + str(attr.value) + ')' 
                i += 1
            elif i == length - 2: ### LEFT HAND SIDE OF RULE
                LHS += name + "_" + str(attr.value) + ')'
                i += 1
            elif i < length- 1: ### LEFT HAND SIDE OF RULE
                LHS += name + "_" + str(attr.value) 
                i += 1
            
            if i < length-1 : 
                LHS += ' , '
        ListOfRules_named.append(complete_rule(LHS,RHS))
        RHS = ''
        LHS = ''
    return ListOfRules_named
###########################################################################################
#function Create_rules
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
###########################################################################################
#function Calculate_Lift
def Calculate_Lift (ListOfLHS, ListOfRHS, ListOfRules):
    length = len(ListOfRules[0])
    ListOfall_s = Calculate_Support(ListOfRules, length)
    ListOfsub1_s = Calculate_Support(ListOfLHS, length-1)
    ListOfsub2_s = Calculate_Support(ListOfRHS, 1)
    s1List = np.array(ListOfall_s)
    s1List = s1List/5822
    s2List = np.array(ListOfsub1_s) ############ LHS Supports List
    s2List = s2List/5822
    s3List = np.array(ListOfsub2_s) ############ RHS Supports List
    s3List = s3List/5822
    ########### Calculate Lift
    ListOfLift = []
    den = s2List * s3List
    i = 0
    for item in s1List:
        Lift = item/den[i]
        ListOfLift.append(Lift)
        i += 1
        
    return ListOfLift
###################################################################
class complete_rule:
    def __init__(self, LHS,RHS):
        self.LHS = LHS
        self.sep = '=>'
        self.RHS = RHS
##########################################################################
def Calculate_Leverage (ListOfLHS, ListOfRHS, ListOfRules):
    length = len(ListOfRules[0])
    ListOfall_s = Calculate_Support(ListOfRules, length)
    ListOfsub1_s = Calculate_Support(ListOfLHS, length-1)
    ListOfsub2_s = Calculate_Support(ListOfRHS, 1)
    s1List = np.array(ListOfall_s)
    s1List = s1List/5822
    s2List = np.array(ListOfsub1_s) ############ LHS Supports List
    s2List = s2List/5822
    s3List = np.array(ListOfsub2_s) ############ RHS Supports List
    s3List = s3List/5822

    ########### Calculate Leverage
    ListOfLeverage = []
    part2 = s2List * s3List
    i = 0
    for item in s1List:
        Leverage = item - part2[i]
        ListOfLeverage.append(Leverage)
        i += 1
        
    return ListOfLeverage
 ################################################## 

min_s = int(input("Enter min Support (%)"))
min_c = int(input("Enter min Confidence (%)"))
attr_values = []

attr_values = Get_atrr_Value()

ListOfListOfAttr = main_fn(attr_values, min_s/100)

combinations = Create_rules(ListOfListOfAttr)

(ListOfLHS ,ListOfRHS, ListOfRules) = Calculate_Confidence(combinations, min_c/100)

LiftList = Calculate_Lift (ListOfLHS, ListOfRHS, ListOfRules)

LeverageList = Calculate_Leverage (ListOfLHS, ListOfRHS, ListOfRules)

ListOfRules_named = Convert_to_name(ListOfRules)


print('{:<40s}{:>4s}{:>15s}{:>15s}{:>15s}'.format("LHS", " " , "RHS" , "Lift" ,"Leverage" ))
r = 0
for item in ListOfRules_named:
    print('{:<40s}{:>4s}{:>15s}{:>15.6f}{:>15.6f}'.format(item.LHS, item.sep , item.RHS , LiftList[r],LeverageList[r]))
    r +=1   
    
    
    
    
    
    
    
    