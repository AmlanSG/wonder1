def peaks(numlist):
    lst=[numlist[0]]

    print (numlist)
    for i in range(0, len(numlist)):
        if  numlist[i] > lst[len(lst)-1]:
            lst.append(numlist[i])

    return lst




numlist = [3, 2, 5, 5, 7, 6, 1, 8, 4]
lst1 = peaks(numlist)
print (lst1)