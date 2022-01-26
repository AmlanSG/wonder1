# Python program to show that we can create
# instance variables inside methods

# Class for Computer Science Student
class CSStudent:
    # Class Variable
    stream = 'cse'


    # The init method or constructor
    def __init__(self, roll, name):
        # Instance Variable/Object Variable
        self.roll = roll   #a.roll =101
        self.name = name   #a.name = "Deb"
        print ("Student Cons called")

    # Adds an instance variable to an exiting or already created object
    def setAddress(self, address):
        self.address = address # a.address = "Kolkata,WB"
        print ("Address called ")

    def setMobile(self, mob):
            self.mob = mob  # a.address = "Kolkata,WB"
            print("Mobile called ")

    # Retrieves instance variable
    def getAddress(self):
        return self.address

    def getmob(self):
        return self.mob
    # Driver Code


a = CSStudent(101, "Ganga")
a.setAddress("Kolkata, WB")
a.setMobile("9999999999")
var = a.getAddress()
var1= a.getmob()
print (var)
print (id(a.address))
print (var1)
print (id(a.mob))
print ("Memory Location of a" ,id(a))

b = CSStudent(102, "Deb")
b.setAddress("Pune, MH")
b.setMobile("1234567890")
print ("Memory Location of b" ,id(b))
var = b.getAddress()
var1 = b.getmob()
print (id (b.address))
print (var)
print (var1)
print (id (b.mob))
print (var)

