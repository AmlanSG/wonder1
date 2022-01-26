class Node:

    # Function to initialise the node object
    def __init__(self, data):
        print("Node Cons Called")
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.flag = 0

# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        print("LL Cons Called")
        self.head = None


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    print ("Initial Head",llist.head)
    first = Node(11)
    print(first)
    llist.head = first
    print("Head Initialized to Node 1", llist.head)
    second = Node(22)
    print (second.data)
    print("Initial Second",second.next)   #####None
    first.next = second;
    print("NEXT Second",second.next)
    third = Node(33)
    second.next = third;
    print("Final Second", second.next)
    fourth = Node(44)
    third.next = fourth

    while (llist.head):
        print(llist.head.data)
        print(llist.head.next)   # first.next
        llist.head.flag = 1
        llist.head = llist.head.next

    print("BREAK")
    ll2 = LinkedList()
    print("Initial Head", llist.head)
    first2 = Node(5)
    ll2.head = first2
    print("Head Initialized to Node 1", llist.head)
    second2 = Node(6)
    first2.next = second2;
    third2 = third
    second2.next = third2;
    fourth2 = Node(8)
    third2.next = fourth2




print ("*********************************************************************")
while (ll2.head):
    if ll2.head.flag == 1:
        print(ll2.head.data)
        print(ll2.head.next)
        break
    ll2.head = ll2.head.next


