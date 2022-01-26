def sum(a,b):
    c=a+b
    print(c)


def func():
    i = 0
    j = 0
    for x in range (0,100):
        sum (i,j)
        i=i+1
        j=j+1

func()


str ="Ganga"
str2 = "Amlan"
print(str==str2)
print (str.__eq__("Ganga"))
print(not str.__eq__("Amlan"))
i = int(input("Enter:"))
print(i)
print(type(i))