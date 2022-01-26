list1 = [1,0,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0]
list2 = [1,0,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0]
list2.sort()
list2.reverse()
print (list2)
l = len(list1)
sum = 0
for i in range(l):
    sum = sum + list1[i]

for i in range (l):
    if sum >0 :
       list1[i] = 1
       sum = sum -1
    else:
       list1[i] = 0

print (list1)