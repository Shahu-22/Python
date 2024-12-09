import numpy as np
print ("hello")
arr=np.array([10,20,30,40,50])
print(arr)
print (type(arr))
print(np.__version__)

#passing tuple in NumPy array:
arrt=np.array((1,2,3,4,5))
print(arrt)

# 2-D array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
# 3-D array
arr2=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr2)

#checking number of dimentions
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)

#higher dimensions
a=np.array([1,2,3,4],ndmin=5)
print("Number of dimension : ",a.ndim)

#Indexing arrays
a1=np.array([1,2,3,4])
print(a1[0])

print(a1[2]+a1[3])

#Access 2-D arrays
a2=np.array([[10,20,30,40,50],[10,30,50,70,90]])
print("2nd element on 1st row :",a2[0,1])
print("2nd row on 5th column :",a2[1,4])

#Access 3-Darrays
a3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a3[0,1,2])

#negative Indexing
print(a2[1,-1])