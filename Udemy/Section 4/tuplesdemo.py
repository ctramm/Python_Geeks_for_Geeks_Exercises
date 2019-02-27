"""
Tuple
Like list but they are immutable
It means you can't change them
"""

my_list = [1, 2, 3]
print("Print my list:")
print(my_list)

my_list[0] = 0
print("\nPrint my list after changing original list:")
print(my_list)

my_tuple = (1, 2, 3, 2, 2, 3)
print("\nPrint my tuple:")
print(my_tuple)

print("\nAccessing my tuple 0th index: ")
print(my_tuple[0])

print("\nSlicing my tuple starting at 1st index: ")
print(my_tuple[1:])

print("\nPrint index of value 2 within my tuple: ")
print(my_tuple.index(2))

print("\nPrint count of my tuple: ")
print(my_tuple.count(3))
