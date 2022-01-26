print("before import")
import math    # __name__ = "Math"

print("before functionA")
def functionA():
    print("Function A On Calling Only")

print("before functionB")
def functionB():
    print("Function B {} on Calling only".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")