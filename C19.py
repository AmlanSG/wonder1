# _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose name starts with an underscore.
#
# single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.
#
# Tkinter.Toplevel(master, class_='ClassName')
#
# __double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).
#
# __double_leading_and_trailing_underscore__: "magic" objects or attributes that live in user-controlled namespaces. E.g. __init__, __import__ or __file__. Never invent such names; only use them as documented.


class Car:
    # Class Variable
    vehicle = 'Car'

    # The init method or constructor
    def __init__(self, model, price):
        # Instance Variable
        self.model = model
        self.price = price

    # Objects of class


Audi = Car("R8", 100000)
BMW = Car("I8", 10000000)

print('Audi details:')
print('Audi is a', Audi.vehicle)
print('Model: ', Audi.model)
print('price: ', Audi.price)

print('\n BMW details:')
print('BMW is a', BMW.vehicle)
print('Model: ', BMW.model)
print('Color: ', BMW.price)

# Class variables can be
# accessed using class
# name also
print("\nAccessing class variable using class name")
print(Car.audi)
