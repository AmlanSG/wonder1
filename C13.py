# Python program to show that the variables with a value
# assigned in class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Computer Science Student

class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name
		print ("Person Cons called")

	def say_hi(self):
		print('Hello, my name is', self.name)

    def walk(self) :
        print('Hello, I am walking', self.name)

class CSStudent:
    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll, name):
        # Instance Variable
        self.roll = roll   #a.roll =101
        self.name = name   #a.name = "Deb"
        print ("Student Cons called")


        # Objects of CSStudent class


a = CSStudent(101,"Deb")
b = CSStudent(102,"Ganga")
c = CSStudent(103,"Amlan")
#d = CSStudent(104)
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)  # prints 101
print(b.roll)

print(a.name)
print(b.name)
# Class variables can be accessed using class
# name also
print(CSStudent.stream)  # prints "cse"
#print(CSStudent.count)


print ("*******************************")
print ("*******************************")
print ("*******************************")

print ("*******************************")
p1 = Person('Ganga')
p1.say_hi()
print ("*******************************")
p2 = Person('Amlan')
p2.say_hi()