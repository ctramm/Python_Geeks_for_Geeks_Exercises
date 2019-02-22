# Python program to demonstrate creation of Sets

# Creating a set
Set1 = set()
print("Initial blank set: ")
print(Set1)

# Creating a Set with the use of a string
Set1 = set('GeeksForGeeks')
print("\nSet with the use of a String: ")
print(Set1)

# Creating a Set with the use of Constructor using object to store string
String = 'GeeksForGeeks'
Set1 = set(String)
print("\nSet with the use of an object: ")
print(Set1)

# Creating a set with the use of a list
Set1 = set(['Geeks', 'For', 'Geeks'])
print("\nSet with the use of List: ")
print(Set1)

# Creating a set with a list of numbers having duplicate values
Set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of numbers: ")
print(Set1)

# Creating a Set with a mixed type of values having numbers and strings
Set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values: ")
print(Set1)
