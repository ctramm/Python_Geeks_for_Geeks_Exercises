# Python code to demonstrate the usage of count() and extend()

import array

arr1 = array.array('i',[1, 2, 3, 1, 2, 5])
arr2 = array.array('i', [1, 2, 3])

# using count() to count occurrences of 1 in array
print("The occurrences of 1 in array is : ", end="")
print(arr1.count(1))

# using extend to add array 2 elements to array 1
arr1.extend(arr2)

print("The modified array is: ", end="")
for i in range(0,9):
    print(arr1[i], end=" ")
