import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
data = pd.read_csv('iris.csv')

# Filter the data for each species
setosa = data[data['species'] == 'setosa']
versicolor = data[data['species'] == 'versicolor']
virginica = data[data['species'] == 'virginica']

# Create a figure with subplots for a histogram of a specific feature (e.g., petal_length)
plt.figure(figsize=(10, 6))

# Plot histograms for 'petal_length' for each species
plt.hist(setosa['petal_length'], bins=10, alpha=0.7, label='Setosa', color='lightblue')
plt.hist(versicolor['petal_length'], bins=10, alpha=0.7, label='Versicolor', color='lightgreen')
plt.hist(virginica['petal_length'], bins=10, alpha=0.7, label='Virginica', color='lightcoral')

# Add labels and title
plt.xlabel('Petal Length (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histogram of Petal Length by Iris Species', fontsize=14)

# Add a legend
plt.legend()

# Show the plot
plt.grid(True, axis='y')
plt.show()
