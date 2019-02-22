# Python program to demonstrate creation of a list

# Creating a list
List = []
print("Initial blank List: ")
print(List)

# Creating a list with the use of a string
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)

# Creating a list with the use of multiple values
List = ['Geeks','For', 'Geeks']
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List by nesting a list inside of a list
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-dimensional List: ")
print(List)

# Creating a list with the use of numbers having duplicate values
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a list with mixed type of values having numbers and strings
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)
