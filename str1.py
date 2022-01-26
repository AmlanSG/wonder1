# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:03:53 2018

@author: ACER
"""
s="Hello!Python" # intializing a string
print(len(s)) # 0,1,,2,12





m="".join(s)

print(m)
# s[0] = "H"
# s[1] = "e"
# s[2] = "l"

print("***********************************")
print (s[6])
print (s[:6])
print (s[2:6]) # slicing # llo!
i=2
j=6
for k in range(i,j):
    print(s[k])



print (s[:]) # Hello!Python

x= 7777777777777
y= 7777777777777
print(x is y) # True
print (x==y)
print(id(x),id(y))



arr=[1,2,0,4,3,0,5,0]
z=[]
k=[]
for i in arr:
    if i==0:
        z.append(i)
    else:
        k.append(i)
for i in z:
    k.append(i)
print(k)