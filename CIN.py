# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def fly(self):
        print("Bird fly faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        #super(Penguin,self).__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin() # "Penguin is ready"
peggy.whoisThis() #
peggy.fly()
peggy.run()
Bd = Bird()
#Bd.run()