import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y=arr.view()
print(y)
arr[0] = 42

print(arr)
print(x)
print(y)

#Shahpe of array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr1=np.array([10,20,30,40],ndmin=5)
print(arr1)
print('shape of array :', arr1.shape)

#Reshaping the arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)
print("1-D to 3-D arrray : ")
newarr = arr.reshape(2, 3, 2)
print(newarr)
#Convert the array into a 1D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)