# LivingBeing -> Animal -> HumanBeing ->Male (Properties + Function)
# Saprrow- Lion - Amar-
# OBJ : Prop, Func/Method-Action
#ls1 = [1,2,3,4,5]
#print (ls1.pop(2)) # this NOT allowed in stack
class Stack1():
    # Ordering => LIFO -> Last In First Out
    def __init__(self): # initialize an empty stack
        print("Empty Stack Created which is empty list")
        self._items = []
# [] => List
    def push(self, item): # add to stack operation
        print ("Push Element",item)
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

    def top(self):
        if not self.is_empty():
           return self._items[-1]
        else:
           return "Stack is Empty so NO top Value"
    def len1(self):
        return len(self._items)

MyS = Stack1()

MyS.push("8")
MyS.push("10")
MyS.push("12")
MyS.push("14")
print ("Before POP",MyS.len1()) #4
print (MyS.pop()) # 14 returns and remove
print(MyS.top())  # 12 only returns
print ("After POP",MyS.len1()) # 3
print (MyS.is_empty()) # False

print (MyS.pop()) # 12
print(MyS.top())# 10
print ("After POP",MyS.len1()) # 2

print (MyS.pop()) #10
print(MyS.top())
print ("After POP",MyS.len1())

print (MyS.pop()) #8
print(MyS.top())
print ("After POP",MyS.len1())

print (MyS.is_empty())
