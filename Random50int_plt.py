import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a random array of 50 integers between 1 and 100
random_data = np.random.randint(1,101,50) 

sns.set(style="whitegrid")

plt.figure(figsize=(14,10))

# 1. Line Chart
plt.subplot(2,2,1)
plt.plot(random_data,marker='o',linestyle='-',color='blue')
plt.xlabel('index')
plt.ylabel('Values')
plt.title('Line Chart')
plt.grid(True)

# 2. Scatter Plot
plt.subplot(2,2,2)
plt.scatter(range(len(random_data)),random_data,marker='x' , color='green')
plt.xlabel('index')
plt.ylabel('Values')
plt.title('Scatter plot')
plt.grid(True)

# 3. Histogram
plt.subplot(2,2,3)
plt.hist(random_data,bins=10,color='orange',edgecolor='blue')
plt.title('Histogram of Random Integers')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 4. Box Plot
plt.subplot(2,2,4)
sns.boxplot(data=random_data,color='purple')
plt.title('Box Plot of Random Integers')

plt.tight_layout()

plt.show()

