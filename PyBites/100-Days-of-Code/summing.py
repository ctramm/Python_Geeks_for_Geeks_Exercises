"""
Bite 1. Sum n numbers
Write a Python function that calculates the sum of a list of numbers:
    The function should accept a list of numbers and return the sum of those numbers.
    If no argument is provided (that is, numbers is None), return the sum of the numbers 1 to 100
    (Note that this is not the same as an empty list of numbers being passed in. In that case the sum returned will be 0).
"""


def sum_numbers(numbers=None):
    if numbers is None:
        results = sum(range(0, 101))
        return results
    else:
        total = 0
        for num in numbers:
            total += num
        return total


if __name__ == '__main__':

    assert sum_numbers() == 5050
    assert sum_numbers(numbers=None) == 5050

    assert sum_numbers(range(1, 11)) == 55
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([]) == 0  # !! [] not the same as None
