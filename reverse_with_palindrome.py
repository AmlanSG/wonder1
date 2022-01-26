b = int(input("Enter How Many Numbers You Like To Reverese "))
a = [ ]

for i in range(0 , b):
  a.append((input("The Number: ")))
print("The Given Number Is: ",a)

c = [ ]

for i in range(0 , len(a)):
  c.append(a.pop())
print("Reverse Of The Given Number Is: ",c)
k="".join(c)
def isPalindrome(c):
  print (c[ : : -1])
  return c == c[ : : -1]

d = isPalindrome(k)

if d:
  print("This is Palindrome.")
else:
  print("This is Not Palindrome.")
