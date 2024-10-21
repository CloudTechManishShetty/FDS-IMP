import pandas as pd

Data = pd.read_csv('Data.csv')
print("The Data Before Filling Missing Value: \n",Data)
print("Column names: ", Data.columns)

mean_salary=Data[' Salary'].mean()
mean_age=Data['Age'].mean()

Data[' Salary'].fillna(mean_salary,inplace=True)
Data['Age'].fillna(mean_age,inplace=True)

print("The Data After Filling Missing Value: \n",Data);