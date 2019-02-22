# Python code to demonstrate the working of index() and reverse()

import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])

print("The newly created array is : ", end="")
for i in range(0,6):
    print(arr[i], end=" ")

print("\r")

# Using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))

# Using reverse() to reverse the array
arr.reverse()

# Printing array after reversing
print("The array after reversing is : ", end="")
for i in range(0,6):
    print(arr[i], end=" ")
