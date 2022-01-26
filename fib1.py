# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:33:58 2018

@author: ACER
"""

a, b = 0, 1
print(a)

N=500
while a < N:

    a,b=b,a+b
    print(a)



##Fib(N) = Fib(N-1) + Fib(N-2)
# 0,1,1,2,3,5,8,13,21
