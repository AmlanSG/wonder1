# Difference between __str__ and __repr__ functions
# __str__ must return string object whereas __repr__ can return any python expression.
# If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
# If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print "Test Cons Called "

    # def __repr__(self):
    # 	print "REPR"
    # 	return "Test a:%s b:%s" % (self.a, self.b)

    def __str__(self) :
        print "String"
        return "From str method of Test: a is %s," 	"b is %s" % (self.a, self.b)

# Driver Code
t = Test(1234, 5678)
print("Not Called ",[t]) # This calls __repr__()
print(t) # This calls __str__()
print type(t)




print "***********************************************"

# class Test:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
# 		print "Test Cons Called "
#
# 	def __str__(self):
# 		return "Wow String: Test a:%s b:%s" % (self.a, self.b)
#
# # Driver Code
# t = Test(1234, 5678)
# print "*****************"
# print(t)



