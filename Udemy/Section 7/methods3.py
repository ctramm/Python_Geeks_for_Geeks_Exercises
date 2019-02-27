"""
Section 7: Positional / Optional Parameters

"""


def sum_nums(n1, n2=4):
    """
    Get sum of two variables
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


x = sum_nums(4, n2=12)
print(x)

