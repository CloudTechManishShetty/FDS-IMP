import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('winequality-red.csv')

# Display the first few rows of the original data
print("Original Data (first 5 rows):")
print(data.head())

# Initialize the StandardScaler
scaler = StandardScaler()

# Standardize the data (excluding non-numeric columns if any)
# Assuming 'winequality-red.csv' has no categorical columns; if there are, drop them
# Fit and transform the data
standardized_data = scaler.fit_transform(data)

# Convert the standardized data back into a DataFrame
standardized_df = pd.DataFrame(standardized_data, columns=data.columns)

# Display the first few rows of the standardized data
print("\nStandardized Data (first 5 rows):")
print(standardized_df.head())
