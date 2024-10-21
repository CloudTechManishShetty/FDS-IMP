import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers between 10 and 100
random_array = np.random.randint(10, 100, 50)

# Add two outliers to the data
random_array_with_outliers = np.append(random_array, [200, 250])  # Adding outliers 200 and 250

# Display the modified box plot
plt.figure(figsize=(6, 4))

# Box plot with outliers
plt.boxplot(random_array_with_outliers, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Box Plot with Outliers', fontsize=14)
plt.ylabel('Value', fontsize=12)

# Display the box plot
plt.show()
