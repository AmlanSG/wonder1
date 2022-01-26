import sys
import os as OperatingSys1
print (OperatingSys1.curdir)
l=[[1,2,3,4,5,6],[7,8,9,0,1,1]]
print (id(l))
print("Size of pointer",sys.getsizeof(l))
for i in range (0,2):
    print((l[i], id(l[i])))
for i in range (0,2):
    for j in range (0,6):
        print( (l[i][j], id(l[i][j])))