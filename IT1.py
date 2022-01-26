# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = ('All', 'For', 'One', 'and', 'One','for','All')
iterable_obj = iter(iterable_value)
print(iterable_obj)
print (type(iterable_obj))
while True:
    try:
        item = next(iterable_obj)
        print (item)
        print (type(item))
    except StopIteration:
        print (" No More Value")
        break


