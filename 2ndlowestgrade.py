l1 = []
index1 =[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append([name,score])
print(l1)
secondmax = []
mx = []
mx.append([max(l1[0][1],l1[1][1]),(1 if l1[0][1] < l1[1][1] else 0)])

secondmax.append([min(l1[0][1],l1[1][1]),0 if l1[0][1] < l1[1][1] else 1])
print (secondmax)
n =len(l1)
for i in range(0,n):
    if l1[i][1]>mx[0][0]:
        k = mx[0][1]
        secondmax.clear()
        secondmax.append([mx[0][0],k])
        mx.clear()
        mx.append([l1[i][1],i])
    elif l1[i][1] > secondmax[0][0] and mx[0][0] > l1[i][1]:
        secondmax.clear()
        secondmax.append([l1[i][1],i])

print(secondmax)