# A optimized school method based
# Python3 program to check
# if a number is prime


def is_prime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


# Driver Program
num1 = 11
num2 = 15
if is_prime(num1):
    print(num1, " is prime")
else:
    print(num1, " is not prime")

if is_prime(num2):
    print(num2, " is prime")
else:
    print(num2, " is not prime")

