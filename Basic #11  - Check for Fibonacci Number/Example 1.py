# Given a number \'n\', how to check if n is a Fibonacci number.
# First few Fibonacci numbers are 0,1,1,2,3,5,8,13,21,34,55,89,141

# Python program to check if x is a perfect square
import math

# A utility function that returns true if x is perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s*s == x


# Returns true if n is a Fibonacci Number, else false
def is_fibonacci(n):
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)


# A utility function to test above functions
for i in range(1,11):
    if (is_fibonacci(i)== True):
        print(i, " is a Fibonacci number")
    else:
        print(i, " is not a Fibonacci number")

