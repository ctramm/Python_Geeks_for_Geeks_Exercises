# Python program to demonstrate addition of elements in a Set

# Creating a set
Set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(Set1)

# Removing elements from Set using Remove() method
Set1.remove(5)
Set1.remove(6)
print("\nSet after removal of two elements: ")
print(Set1)

# Removing elements from Set using Discard() method
Set1.discard(8)
Set1.discard(9)
print("\nSet after Discarding two elements: ")
print(Set1)

# Removing elements from Set using iterator method
for i in range(1,5):
    Set1.remove(i)
print("\nSet after removing a range of elements: ")
print(Set1)

# Removing element from the Set using the pop() method
Set1.pop()
print("\nSet after popping an element: ")
print(Set1)

# Removing all the elements from Set using clear() method
Set1.clear()
print("\nSet after clearing all the elements: ")
print(Set1)
