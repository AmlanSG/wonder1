# Python program to
# demonstrate implementation of
# queue using queue module


from queue import Queue

# Initializing a queue
q = Queue(maxsize = 9)

print (type(q))
# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue a,b,c,d,e <-
for i in range(1,10):
    q.put(i)

# Return Boolean for Full
# Queue
print("\nFull: ", q.full()) 

# Removing element from queue
print("\nElements dequeued from the queue")
while (not q.empty()):
    print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)

print("\nEmpty: ", q.empty())
print("Full: ", q.full())
q.get()

print(q.get())
