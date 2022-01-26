from copy import deepcopy

lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
lst2[2][1]= "What"
lst4 = lst1
lst4[0] = "H"
print id(lst1)
print id(lst4)

print lst1
print lst4

lst3 = lst1[:]

lst3[2][1] = "Z"

print lst1
print lst2
print lst3
print(id(lst1[2][1]))
print(id(lst2[2][1]))
print(id(lst3[2][1]))
