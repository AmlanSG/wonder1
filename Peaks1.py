def peaks(numlist):
# Run loop from 0 to len/2
    lst= [None] * len(numlist)
    print (lst)
    print (numlist)
    for i in range(len(numlist)-1):
         if  numlist[i] > numlist[i-1]:
            lst.append(numlist[i])
    return lst




print (peaks([3, 2, 5, 5, 7, 6, 1, 8, 4]))