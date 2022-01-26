SetX = {1,2,3,4,5,6,7,8,99,98}
SetY = {99,98,97,96,95,94,93,1,2}
Vset = SetX.union(SetY)
print (Vset)
Vset2 = SetX.intersection(SetY)
print (Vset2)

Vset3 = SetX.difference(SetY)
print (Vset3)

Vset3 = SetY.difference(SetX)
print (Vset3)
SetA = {1,2,3,4,5,6}
SetB = {2,3,4}
SetC = {99,98,97}
print (SetA.isdisjoint(SetC))
print (SetA.issubset(SetB))
print (SetB.issubset(SetA))
