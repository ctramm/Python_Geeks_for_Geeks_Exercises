"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers.
"""

print(list(range(0, 10)))

a = range(10, 20, 2)
print(a)
print(type(a))

print(list(a))

for num in range(1, 4):
    print(num)
