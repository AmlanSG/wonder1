str1 ="hELLOWorld"
rval =""
l1 =list(str1)
print (l1)
for c in l1:
    if c.isupper() == True :
        rval += c.lower()
    else:
        rval += c.upper()

print(rval)




