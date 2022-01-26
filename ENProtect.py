class Base:
    def __init__(self):
        # Protected member
        self._a = 2
        print "I'm in Base Class" , self._a
    def gan (self):
        print " Method in Base class" , self._a

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print "^^^^^^After base Class"
        print("Calling protected member of base class: ")

        print("Calling from Inside Derived Class", self._a)
    def gan (self):
        print " Method in Derived class" , self._a

obj1 = Derived()

obj2 = Base()

# Calling protected member
# Outside class will result in
# AttributeError
# calling from outside class

print "*************************************************************"
print obj2.gan()
print obj1.gan()
print(obj2.a)

print(obj1.a)
print "*************************************************************"



