# Python3 program to remove duplicate
# tuples from list of tuples


def removeDuplicates(lst):
    return list(set([i for i in lst]))


# Driver code
lst = [('a', 'z'), ('a', 'x'), ('z', 'x'), ('a', 'x'), ('z', 'x')]
print(removeDuplicates(lst))


# Python3 code to demonstrate working of
# Get unique tuples from list
# using set() + list()

# initializing list
test_list = [(4, 5), (6, 1), (4, 5), (6, 1)]

# printing original list
print("The original list is : " + str(test_list))

# Get unique tuples from list
# using set() + list()
res = list(set(test_list))

# printing result
print("List after removal of duplicates " + str(res))
