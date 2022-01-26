import time
x = ["a","b","c"]
y= [x]*4
print y
print y[1][1]
y[2][2] = "Z"
print y

print id(y[0][1])
print id(y[1][1])
print id(y[2][1])
print id(y[0])
print id(y[1])
print id(y[2])


n= 100000
start_time = time.time()
l = list()
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)
start_time = time.time()
l = list()
for i in range(n):
    l += [i * 2]

print(time.time() - start_time)
start_time = time.time()
l = list()
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)

list1 = ['a','b','c','d']
list2 = list1
list3 = list1[:]
print (id(list1))
print (id(list2))
print (id(list3))
list2[1] = "z"
print (list1)
print (list2)
print (list3)







