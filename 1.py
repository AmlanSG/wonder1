# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:34:42 2018

@author: ACER
"""

lst1 =["New Delhi",2,"Pune","hydrbad"]
print lst1


com_list = ["ab",["b",["c",["x"]]],"48"]
for i in range (0, len(com_list)):
    print com_list[i][1]
print (len (com_list))
new_list = com_list.extend(lst1)
print(com_list)
print(len(com_list))

x=["a","b","c"]
z= x*3
print(z)
y=[x]*3
print(y)
y[1][2]= "P"
print(y)
print(id(y[0]),id(y[1]))