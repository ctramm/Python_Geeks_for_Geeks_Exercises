"""
Section 7: Functions/Methods - Working with Reusable Code

A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""


def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


x = sum_nums(2, 8)
y = sum_nums(3, 3)
st = sum_nums('one', ' two')

print(x)
print(y)
print(st)


def is_metro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False


print('*' * 20)
z = is_metro('boston')
print(z)


