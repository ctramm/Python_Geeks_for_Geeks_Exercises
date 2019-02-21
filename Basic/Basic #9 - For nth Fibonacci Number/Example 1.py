# In mathematical terms, the sequence of Fn of Fibonacci numbers is defined by the recurrence relation
# Fn = Fn-1 + Fn-2
# with seed values
# F0 = 0 and F1 = 1.

# Method 1 (Use recursion)
# Function for nth Fibonacci number


def fibonacci(n):
    if n < 0 :
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Driver Program
num = 27
print(fibonacci(num))
