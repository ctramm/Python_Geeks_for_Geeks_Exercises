# Python code to demonstrate the working of
# typecode, itemsize, buffer_info()

import array

arr = array.array('i',[1, 2, 3, 1, 2, 5])

# using typecode to print itemsize of array
print("The datatype of array is: ", end="")
print(arr.typecode)

# using itemsize to print itemsize of array
print("The itemsize of array is: ", end="")
print(arr.itemsize)

# using buffer_info() to print buffer info of array
print("The buffer info of array is :", end="")
print(arr.buffer_info())
