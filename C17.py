class Person:
    name = "Amlan"
    age = 40
    def foo (self):
        print ("Hi Rashmi")

    def foo1():
        print("Hi Neha")

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    # def __str__(self):
    #     print "String"
    #     return self.name

    def __repr__(self):
        print( "REPR")
        return str(self.age)


p = Person('Neha', 20)
print (p.name)
print (p.age)

print(Person.name)
print(Person.age)


# p1 = Person()
# print p1.age
# print p1.name
print(p)
p.foo()
#print("Return Value ", p)
