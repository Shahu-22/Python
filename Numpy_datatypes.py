import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype,"\n")
arr = np.array([1, 2, 3, 4])

print(arr.dtype)

#Create an array with data type string:
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
#Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
#Converting datatype of array 
arr = np.array([11.1,  12.1, 13.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)