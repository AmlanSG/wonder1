cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print cities
#sets can't contain mutable objects
#sets are mutable

#cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
#my_set4 = {1, 2, [3, 4]}

my_set5 = set([1,2,3,2])
print "***************************"
print my_set5
print "***************************"
print my_set5[0]




#A set in python is a data structure that contains an unordered collection of unique and immutable objects.

x = set( 'A Java Tutorial' )
print x

#Frozensets are like sets except that they cannot be changed, i.e. they are immutable:


my_string = 'foobar'
setA = set(my_string)
print setA
print dir(setA)
#Set cannot have mutable items. Here [3, 4] is a mutable list:



SetX = {1,2,3,4,5,6,7,8}
print SetX
SetX.add((9,10))
print SetX
SetX.update([11,12])
print SetX
SetX.discard(3)
print SetX
SetX.remove(6)
print SetX
SetX.discard(3)
print SetX
SetX.remove(6)

my_set8 = set('HelloWorld')

v1 = my_set8.pop()

print v1
print my_set8
my_set8.clear()
print my_set8

numbers={1,2,3,4}
new_numbers=numbers
new_numbers.add(5)
print('numbers:',numbers)

SetX.update([1, 2, 3, 4, 5, 10, 15, 22])
print SetX
SetY = {99,98,97,96,95,94,93}
SetX.update(SetY)
print SetX

print(SetX & SetY)
SetX.intersection(SetY)
print SetX

SetX.difference(SetY)
print SetX

print SetX.isdisjoint(SetY)
print SetX.issubset(SetY)
print SetY.issubset(SetX)

cities1 = frozenset(["Hyderabad", "Bangalore","Chennai"])
cities1.add("Delhi")