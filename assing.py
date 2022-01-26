c = 15
d = 10
a = 2
b = 3


print ("Memory of c and d", id(c),id(d))
c,d = d,c

# Multiple assingmnet


#c=d
#d=c
print ("This is originally d and NEW c",c)
print ("This is originally c and New d",d)
print ("Memory of c and d", id(c),id(d))


#####################################
a=5
b=7
a,b=a+2,a-1
print (a) # 7
print(b) # 4
c=5
d=7
c=c+2
d=c-1
print (c) #7
print(d) #6


#Fib(N) = Fib(N-1) + Fib(N-2)
# 0,1,1,2,3,5,8,13, 21