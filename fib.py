# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:33:58 2018

@author: ACER
"""

a, b = 0, 1   # fixed time, time is not proportional to "N"
print(a)     # fixed , time is not proportional to "N"
print(b)     # fixed, , time is not proportional to "N"
N=500000   # Input Size grows -> Infinity
while b < N:
    print(b)
    a,b=b,a+b
print('Hello Fib')
# fib will take time proportional to N
# fact will take time proportional to N^2  - just an example





c = 15
d = 10
c,d = d,c


#c=d
#d=c
print (c)
print (d)
