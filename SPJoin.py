# Python program to split a string and
# join it using different delimiter

def split_string(string):
    # Split the string based on space delimiter
    list_string = string.split(' ')

    return list_string


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '-'.join(list_string)

    return string


# Driver Function
if __name__ == '__main__':
    string = 'Geeks for Geeks'

    # Splitting a string
    list_string = split_string(string)
    print(list_string)

    # Join list of strings into one
    new_string = join_string(list_string)
    print(new_string)



# Python3 code to demonstrate working of
# Split string on Kth Occurrence of Character
# Using split() + join()

# initializing string
test_str = "Geeks_for_Geeks_is_best"

# split char
splt_char = "_"
# lst1 = test_str.split(splt_char)
# print lst1
# initializing K
K = 3

# printing original string
print("The original string is : " + str(test_str))

# Using split() + join()
# Split string on Kth Occurrence of Character
temp = test_str.split(splt_char)
res = splt_char.join(temp[:K]), splt_char.join(temp[K:])

# printing result
print("Is list after Kth split is : " + str(list(res)))
