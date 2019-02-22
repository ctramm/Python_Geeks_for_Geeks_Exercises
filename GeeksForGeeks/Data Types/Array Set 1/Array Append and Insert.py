# Python code to demonstrate the working of array(), append(), insert()

# Importing "array" for array operations
import array

# Initializing array with array values
# Signed Integers
arr = array.array('i', [1, 2, 3])

# Printing original array
print("The newly created array is : ", end=" ")
for i in range (0, 3):
    print(arr[i], end=" ")
print("\r")

# using append() to insert new value at end
arr.append(4)

# Printing appended array
print("The appended array is : ", end="")
for i in range(0,4):
    print(arr[i], end=" ")

# Using insert() to insert value at specific position
# Insert 5 at 2nd position
arr.insert(2, 5)

print("\r")

# printing array after insertion
print("The array after insertion is : ", end="")
for i in range (0, 5):
    print(arr[i], end=" ")


