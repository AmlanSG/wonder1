##class Concept:
  ##  prop:

    ## methods: Object.Method()







# A simple example class
class Test:

    # A sample method
    def fun(self):       #Self is always the object that is calling the method in the Class
        print("Hello")

    # Driver code

class Bird:
    # init method or constructor
    def __init__(self, name):
       self.name1 = name
       print("Cons called, Bird Initialized Demo For Diip, Rashmi And Neha")
    def fly(self):
        print (self.name1 ," is flying")

    def sing(self):
        print (self.name1 ," is singing")
parrot = Bird("Mitu")
print("1.**********************************************")
parrot.fly()
parrot.sing()

parrot2 = Bird("Tota")
print("2nd Parrot.**********************************************")
parrot2.fly()
parrot2.sing()
print (type(parrot))
crow = Bird("BlackJack")
print("2. **********************************************")
crow.fly()
crow.sing()
print (type(crow))
reshmi = Test()
reshmi.fun()
neha = Test()
neha.fun()
lst1 = list()



