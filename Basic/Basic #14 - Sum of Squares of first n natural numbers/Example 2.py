# Python program to find sum of square of first n natural numbers

# Return the sum of square of first n natural numbers
def square_sum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Driver Code
n = 4
print(square_sum(n))
