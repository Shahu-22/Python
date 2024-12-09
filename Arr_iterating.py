import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
  print(x)
#Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
#Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
#using nditer function
 arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)   