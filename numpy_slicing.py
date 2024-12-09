import numpy as np 
arr=np.array([1,2,3,4,5])
print("array is : ",arr)
print("\n",arr[1:5])
print("\n",arr[4:])
print("\n",arr[:4])

#negative slicing
print("\n",arr[-3:-1])

#step assigning
print("\n",arr[1:5:2])
print("\nonly step : ",arr[::2])

#slicing with 2-D arrays
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#print(arr2)
print(arr2[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
print(arr[0:2,1:4])
