print dir(BaseException)
print BaseException.__subclasses__()
print "********************************************"
print Exception.__subclasses__()

arr= [0,1,2,0,0,4,0,5]
p = []
while 0 in arr:
    p.append(0)
    arr.remove(0)
#Loop finishes
arr=arr+p
print arr

