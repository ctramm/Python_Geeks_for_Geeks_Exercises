# Python code to demonstrate the usage of fromlist() and tolist()

import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])
li = [1, 2, 3]

# using fromlist() to append list at the end of array
arr.fromlist(li)

# Printing the modified array
print("The modified array is:", end="")
for i in range (0,9):
    print(arr[i], end=" ")

# using tolist() to convert array into list
li2 = arr.tolist()
print("\r")

# Printing the new list
print("The new list created is: ", end="")
for i in range(0,len(li2)):
    print(li2[i], end=" ")

