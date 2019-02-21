# Python program to demonstrate accessing of element from list

# Creating a list with the use of multiple values
List = ['Geeks', 'For', 'Geeks']

# Accessing an element from the list using index number
print("Accessing an element from the list")
print(List[0])
print(List[2])

# Creating a multi-dimensional list by nesting a list inside a list
List = [['Geeks', 'For'], ['Geeks']]

# Accessing an element from the multi-dimensional list using index number
print("\nAccessing an element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing an element using negative indexing
print("\nAccessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the 3rd last element of list
print(List[-3])
