ls1 =[]
i = int(input("Please Give the Number"))
for j in range (0,i):
    ls1.append(input())

print ("".join(ls1))
a=[]
for j in range(len(ls1)):
  a.append(ls1.pop())
print ("".join(a))
#ABA