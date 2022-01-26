# Python program to
# demonstrate queue implementation
# using collections.dequeue


from collections import deque

# Initializing a queue
q = deque()
print (type(q))
print(q.__len__())
if q.__len__() ==0:
    print ("Queus is Empty")
# Adding elements to a queue
for i in range (0,10):
    q.append(i) # enqueue

####     F e1,e2,e3....R   <-
print("Initial queue")
print(q)
if q is None:
    print ("Queus is Empty")
# Removing elements from a queue
print("\nElements dequeued from the queue")
while (q.__len__() !=0):
    print(q.popleft())


print("\nQueue after removing elements")
print(q)

#print(q.popleft())

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty
