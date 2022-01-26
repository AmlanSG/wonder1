# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        print "Cons Base Class"
        self.a = "GeeksforGeeks"
        print "Private Variable "
        self.__c = "GeeksforGeeks"



# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        self.__d = "GeeksforGeeksDerived"
        print(self.__d)
        print "Private member of Base Class"
        print(self.__c)
    # Driver code


obj1 = Base()
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
print(obj1.a)
print "*********************************"
drv1 = Derived()
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
print drv1.a
# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
