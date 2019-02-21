# Python program to demonstrate addition of elements in a list

# Creating a list
List = []
print("Initial blank list:")
print(List)

# Addition of Elements in the list
List.append(1)
List.append(2)
List.append(4)
print("\nList after addition of three elements: ")
print(List)

# Adding elements to the list using iterator
for i in range(1,4):
    List.append(i)
print("\nList after addition of elements from 1-3: ")
print(List)

# Adding Tuples to the list
List.append((5, 6))
print("\nList after Addition of a tuple: ")
print(List)

# Addition of list to a list
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after addition of a list: ")
print(List)

# Addition of Element at specific position using insert method
List.insert(3, 12)
List2.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)

# Addition of multiple elements to the list at the end using extend method
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend operation: ")
print(List)
