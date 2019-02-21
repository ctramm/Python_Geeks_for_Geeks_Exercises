# Print the sum of series 1 ** 3 + 2 ** 3 + 3 ** 3 + 4 ** 3 + ... + n ** 3


# Returns the sum of series
def sum_of_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    return sum


# Driver
n = 5
print(sum_of_series(n))

