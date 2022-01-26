# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)


# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)
