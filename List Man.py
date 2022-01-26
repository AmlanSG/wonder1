# The main properties of Python lists:
# They are ordered/queued
# The contain arbitrary objects
# Elements of a list can be accessed by an index
# They are arbitrarily nestable, i.e. they can contain other lists as sublists
# Variable size
# They are mutable, i.e. the elements of a list can be changed

arblist = list([1,2]) # [1,2]
print (arblist)
print ("Class of the object", type(arblist))   # List
arblist = [9,2, "Delhi", 'Pune', ''' Bangalore ''']
print ("Class of the object", type(arblist[2])) # str
print (arblist)
print (arblist[3])

lst = [3, 5, 7]
lst.append(42)
print("New Appended List",lst)
#print lst.__doc__
print(lst.append(45))
var = lst.append(50)
print (" Prints the return value" , var)
print(" Prints the final list NEW" , lst)
print ("********************************************")
cities = ["Delhi", "Linz" ,"Pune", "Vienna","Kolkata","Ranchi"]
print ("Slicing Experiment 1:",cities[::])
print ("Slicing Experiment 2:",cities[::-2])
print(cities.pop(2))
print(cities)
print (cities.pop(len(cities)-1))
print (cities)
print (cities[1])
cities.pop(0)
print (cities)
#cities.pop(1)
print (cities)




lst = [42,98,77]
lst.append("v") # adding to existing list
lst.append("A")
print (lst)
lst2 = [8,69]
lst3 = ["R","D"]
lst.append(lst2)
lst.append(lst3)
lst.append("RIG")
print("Lets chk Reshmi", lst) # [42, 98, 77, 'v', 'A', [8, 69]]


lst1 = [42,98,77]
lst2 = [8,69]
lst1.extend(lst2)
print("Lets chk Rig", lst1)


lst = ["a", "b", "c"]
programming_language = "123"
lst.extend(programming_language)
print(lst)
print (lst.__class__)
print(type(lst))# obj.method , function(obj)

lst = ["a", "C", "d"]
t = ("C#", "Jython", "Python", "IronPython")  # Tuple
lst.extend(t)
print (lst)

colours = ["red", "green", "blue", "green", "yellow","green"]
p = colours.count("green")
print (p)
colours.remove("blue")
print (colours)
colours.pop(3)
print ("Blue removed and 3 is poped",colours)
#colours.remove("Black")
colours = ["red", "green", "blue", "green", "yellow"]
print (colours.index("green"))

print (colours.index("green", 2))

print (colours.index("green", 3,4))

#print (colours.index("White"))
lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
print(lst)

p = lst.count("Austria")
print (p)
var = int(input("Enter Integer"))
print(type(var))
print ("Input Variable is " + str(var))
print (var+2)

str1 = "amlan"
ival = str1.count("a")
print ( ival)


