import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Data.csv')

# Plotting a line graph for Name vs Salary
plt.figure(figsize=(10,6))
plt.plot(data['Name'], data[' Salary'], marker='o', linestyle='-', color='b')

# Adding labels and title
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Name vs Salary Line Plot')

plt.show()
