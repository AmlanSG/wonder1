class Mechanism(object):
    def __init__(self):
        super(Mechanism, self).__init__()
        print('Init Mechanism')
        self.__mechanism = 'this is mechanism'

    def get_mechanism(self):
        return self.__mechanism

class Vehicle(object):
    def __init__(self):
        super(Vehicle, self).__init__() # didn't print
        print('Init Vehicle')
        self.__vehicle = 'this is vehicle'

    def get_vehicle(self):
        return self.__vehicle

class Car(Mechanism, Vehicle):
    def __init__(self):
        super(Car, self).__init__()
        print "Car Called"

c = Car()
print "**********************************"
print(c.get_mechanism())
print(c.get_vehicle())
