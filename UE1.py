# A python program to create user-defined exception

# class MyError is derived from super class Exception
class MyError(Exception):

	# Constructor or Initializer
	def __init__(self, value):
		self.value = value
		print "Inside Cons"

	# __str__ is to print() the value
	def __str__(self):
		print "Inside String"
		return(repr(self.value))


try:
	#print "B4 Exception"
	if 2>0:
		raise(MyError(3*2))
    #print "After Exception No Print"

# Value of Exception is stored in error
except MyError as error:
	print error.__str__()
	print('A New Exception occured: ',error.value)
