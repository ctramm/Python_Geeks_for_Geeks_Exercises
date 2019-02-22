# Given a number x, determine whether the given number is Armstrong number or not.
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n)+ ....


# Function to calculate x raised to the power y
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y / 2) * power(x, y / 2)
    return x * power(x, y / 2) * power(x, y / 2)


# Function to calculate order of the number
def order(x):
    # Variable to store order of the number
    n = 0
    while x != 0:
        n = n + 1
        x = x / 10
    return n


# Function to check whether the given number is
# Armstrong number or not
def is_armstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while temp != 0:
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp / 10

    # If condition satisfies
    return sum1 == x


# Driver Code
x = 153
print(is_armstrong(x))
x = 1253
print(is_armstrong(x))
