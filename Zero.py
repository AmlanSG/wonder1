def pushZerosToEnd(arr, n):
    count = 0  # Count of non-zero elements
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1    # count = count + 1
    print("1st Shift",arr)
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1


# Driver code
arr = [0,1,0,2,0,3,4,0,0,0,7,8,9,0,0,4]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)