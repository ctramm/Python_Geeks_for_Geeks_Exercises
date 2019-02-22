# Python program to demonstrate removal of elements in a list

# Creating a list
List = ['G', 'E', 'E', 'K', 'S',
        'F', 'O', 'R',
        'G', 'E', 'E', 'K', 'S']
print("Initial List:")
print(List)

# Print elements of a range using Slice operation
Slice_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Slice_List)

# Print elements from beginning toa  pre-defined point using Slice
Slice_List = List[:-6]
print("\nElements sliced til 6th element from last: ")
print(Slice_List)

# Print elements from a pre-defined point to end
Slice_List = List[5:]
print("\nElements sliced from 5th element til the end: ")
print(Slice_List)

# Printing elements from beginning til end
Slice_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Slice_List)

# Printing elements in reverse using slice operation
Slice_List = List[::-1]
print("\nPrinting list in reverse: ")
print(Slice_List)
