# Python program to demonstrate removal of elements in a list

# Creating a list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial List:")
print(List)

# Removing elements from list using Remove() method
List.remove(5)
List.remove(6)
print("\nList after removal of two elements: ")
print(List)

# Removing elements from list using iterator method
for i in range(1,5):
    List.remove(i)
print("\nList after removing a range of elements: ")
print(List)

# Removing element from the set using the pop() method
List.pop()
print("\nList after popping an element:")
print(List)

# Removing element at a specific location from the set using the pop() method
List.pop(2)
print("\nList after popping a specific element:")
print(List)

