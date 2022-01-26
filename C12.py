# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name
		print ("Cons called")
	# def __init__(self):
	# 	print "Default Cons"
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Shwetanshu')
p.say_hi()

print( "*******************************")
p1 = Person('Ganga')
p1.say_hi()
print ("*******************************")
p2 = Person('Amlan')
p2.say_hi()
print ("*******************************")
po = Person("Deb")
po.say_hi()