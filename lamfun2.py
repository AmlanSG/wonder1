# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))

print(adults)
