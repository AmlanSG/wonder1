StrO = "ABRACADABRA"
StrF = 'RA'
print (StrO.count(StrF))

res1 = [[x, y] for x in [1, 2, 3,5,7] for y in [0,2,4, 5, 6]]
print(res1)
for i in range(len(res1)):
    if res1[i][0] + res1[i][1] == 7:
        print (res1[i])
