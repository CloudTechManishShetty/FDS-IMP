import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
data = pd.read_csv('iris.csv')

# Get the frequency of each species
species_count = data['species'].value_counts()

# Create a bar plot for species frequency
plt.figure(figsize=(8, 6))
species_count.plot(kind='bar', color=['lightblue', 'lightgreen', 'lightcoral'])

# Add labels and title
plt.xlabel('Species', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Frequency of Iris Species', fontsize=14)

# Show the plot
plt.grid(True, axis='y')
plt.show()
