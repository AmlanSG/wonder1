import re
pattern = '^[9,8,7]'
test_string = '2066543216'
result1 = re.match(pattern, test_string)
print (result1)
if result1 and len(test_string) == 10:
    print("Valid Mobile Number.")
else:
    print("NOT Valid Mobile Number.")
print (sum(range(int(input()) + 1)))