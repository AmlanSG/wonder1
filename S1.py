cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print (cities)
#print (cities[2])
# #sets can't contain mutable objects
# #sets are mutable
#
#cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
#my_set4 = {1, 2, [3, 4]}
#
my_set5 = set([1,2,3,2])
# print "***************************"
print (my_set5)
# print "***************************"
#print (my_set5[0])

x = set( 'A Java Tutorial' )
print (x)
lst1=[]
for i in range(len(x)):
    y = x.pop()
    lst1.append(y)
print (y)
print (lst1)
print (x)


my_string = 'foobar'
setA = set(my_string)
print (setA)
print (dir(setA))

