# Python 3 program to find
# factorial of given number
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


# Driver Code
num = 5;
print("Factorial of", num, "is",factorial(num))

# fact(5) = fact(4) * 5
# fact(6) = fact(5) * 6
# fact(N) = fact(N-1) * N


