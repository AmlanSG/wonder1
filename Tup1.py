#Tuples are identical to lists in all respects, except for the following properties:

#Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
#Tuples are immutable.

# Why use a tuple instead of a list?
#
# Program execution is faster when manipulating a tuple than it is for the equivalent list. (This is probably not going to be noticeable when the list or tuple is small.)


t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

t1 = "Amlan","Diipanjan","Vedh","Neha"
# amlan
print (type(t))
print (type(t1))
print ("Print fourth Last Element:", t[-4])
#t[2] = 'Bark!'

print ("1st rev", t[::-1])
lst1 = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print (" print straight", lst1[::1])
print ("list rev", lst1[::-1])

str1 = "Amlan Sengupta"
print (str1[::-1])

for i in range (0,4,1):
    print (lst1[i])

for i in range (len(lst1)-1,-1,-1):
    print ("EXp with Loop",lst1[i])

for i in range (len(lst1)-1,-1,-1):
    print (lst1[i])


str2=""

for i in range (len(str1)-1,-1,-1):
    str2 = str2 + str1[i]

print (" Treat 4 Diip and Reshmi", str2)

t4 = (2)
print (type(t4))
t5 = 2,

print (type(t5))
#unpacking of tuple
(s1, s2, s3, s4, s5,s6) = t
#t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print ("After Unpacking Tuple", s1, s2, s3, s4, s5, s6)
print(s1)
print(s2)
print(s3)
print(s4)

print (t.index("baz"))
t.__add__(("Deep",))

print (t)







