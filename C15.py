class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        # self.__hiddenVariable  = self.__hiddenVariable  + increment
        print ("Printing Hidden Variable from inside class", self.__hiddenVariable)

    # Driver code


myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
print (MyClass.__hiddenVariable)
# This line causes error
print (myObject.__hiddenVariable)
