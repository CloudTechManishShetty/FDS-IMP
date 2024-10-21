import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv');

species_counts = iris_data['Species'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(species_counts,labels=species_counts.index,autopct='%1.1f%%', startangle=90, colors=['green','blue','purple'])
plt.title("Frequency of iris Species")
plt.axis('equal')
plt.show()