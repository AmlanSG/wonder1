__metaclass__ = type
class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age
        print "I am Person"

    def __str__(self):
        print "I am alternate person"
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):
    def __init__(self, first, last, age, staffnum):
        super(Employee, self).__init__(first, last, age)
        self.staffnumber = staffnum
        print "I am Employee"
    def __str__(self):
        print "I am Alternate Employee"
        return super(Employee, self).__str__() + ", " +  self.staffnumber


x = Person("Marge", "Simpson", 36)
print "*******************"
print "*******************"

y = Employee("Homer", "Simpson", 28, "1007")

print "*******************"
print "*******************"

print(x)

print "*******************"
print(y)