# Given two positive integer start and end.
# The task is to write a python program to print all Prime numbers in an interval.
#
# Definition: A prime number is a natural number greater tahn 1 that has no positive divisors other than 1 and itself.
# The first few prime numbers are {2, 3, 5, 7, 11...)
#
# The idea to solve this problem is to iterate the val from start to end using a for loop and for every every number,
# if it is greater than 1, check if it divides n. If we find any other number which divides, print that value.

# Python Program to print all
# prime number in an interval

start = 11
end = 250

for val in range(start, end +1):
    # If num is divisible by any number
    # between 2 and val, it is not prime
    if val > 1:
        for n in range(2,val):
            if (val % n) == 0:
                break
        else:
            print(val)

