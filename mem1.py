# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:43:28 2018

@author: ACER
"""

x=4
y=4
print (id(x),id(y))

arr = [1,2,2,2, 3,4,5,9]
print(arr.index(4,0,len(arr)-1))
print(arr.count(2))
arr.remove(4)
arr.count(2)
print(arr)

arr.append(12) # PUSH
print(arr)
arr1 = arr.copy()
print(arr1)