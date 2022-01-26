# -*- coding: utf-8 -*-
"""
Created on Sun May 06 15:24:50 2018

@author: ACER
"""
# variable
x=40
y=40
z =40
print ("Amlan")
print (type(x))
print (type(y))
print ("The address of x,y,z",id(x),id(y), id(z))
x="Ganga"
y="Ganga"
print ("Amlan")
print (x)
print (y)
print ( id(x),id(y))

print ("++++++++++++++++++++++++++++++++++++++++")

a=int(input()) #element to be inserted
l=[1,2,3,4,5]
p=3
#let l is the array and p is the index at which element has to be inserted
l=l[:p]+[a]+l[p:]
print (l)
