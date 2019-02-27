"""
Section 7: More Built-In Functions

Some built-in functions
max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

asb(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument.

"""


def largest_num(*args):
    print(max(args))
    return max(args)


largest_num(1, 2, 5, 9, 12354, -20, 0)


def smallest_num(*args):
    print(min(args))


smallest_num(1, 2, 5, 9, 12354, -20, 0)


def abs_num(arg):
    print(abs(arg))


abs_num(-20)
abs_num(20)

print('*' * 20)

print(type(99))
print(type(99.9))
print(type('99.9'))
li = [1, 2, 3]
print(type(li))
