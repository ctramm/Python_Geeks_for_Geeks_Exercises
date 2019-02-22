# Python program to demonstrate addition of elements in a set

# Creating a set
Set1 = set()
print("Initial blank set: ")
print(Set1)

# Adding element to the Set
Set1.add(8)
Set1.add(9)
Set1.add(12)
print("\nSet after addition of three elements: ")
print(Set1)

# Adding elements to the set using Iterator
for i in range(1,6):
    Set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(Set1)

# Adding Tuples to the Set
Set1.add((6, 7))
print("\nSet after Addition of a Tuple: ")
print(Set1)

# Addition of elements to the set using update function
Set1.update([10, 11])
print("\nSet after addition of elements using update: ")
print(Set1)
