import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_data = pd.read_csv('iris.csv')

# Set the plot style
sns.set(style="whitegrid")

# Create a figure and axes to plot
plt.figure(figsize=(14,10))

# Create a box plot for each feature grouped by species
plt.subplot(2, 2, 1)
sns.boxplot(x='Species', y='SepalLengthCm', data=iris_data)
plt.title('Sepal Length Distribution')

plt.subplot(2, 2, 2)
sns.boxplot(x='Species', y='SepalWidthCm', data=iris_data)
plt.title('Sepal Width Distribution')

plt.subplot(2, 2, 3)
sns.boxplot(x='Species', y='PetalLengthCm', data=iris_data)
plt.title('Petal Length Distribution')

plt.subplot(2, 2, 4)
sns.boxplot(x='Species', y='PetalWidthCm', data=iris_data)
plt.title('Petal Width Distribution')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
