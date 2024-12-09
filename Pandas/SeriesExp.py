import pandas as pd
a = [1, 7, 2]
myList = pd.Series(a)
print(myList)
#Lebeling Indexes
myList=pd.Series(a,index=['a','b','c'])
print(myList)
#Key value series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
#Creating DataFrames in pandas
data={
    "Student":['s1','s2','s3'],
    "Marks":[90,91,92]
}
d=pd.DataFrame(data)
print(d)