import pandas as pd

data = {
  "Name": ["Shahu","Amey","Shubham"],
  "Marks": [90,95,96]
}

df = pd.DataFrame(data, index = ["s1", "s2", "s3"])

print(df) 
print("student at index 2 : ",df.loc['s2'])

#Creating new csv file
df.to_csv('Student.csv',index=False)

#Reading csv file
print(pd.read_csv('Student.csv'))