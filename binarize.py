import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Binarizer

# Load the wine quality dataset
data = pd.read_csv('winequality-red.csv')

# Display the first 5 rows of the original dataset
print("Original Dataset:\n", data.head())

### Task a: Rescaling using MinMaxScaler ###
# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Apply MinMaxScaler to rescale the dataset (excluding the target column 'quality')
data_rescaled = pd.DataFrame(scaler.fit_transform(data.iloc[:, :-1]), columns=data.columns[:-1])

# Add the target column back to the rescaled data
data_rescaled['quality'] = data['quality']

# Display the first 5 rows of the rescaled dataset
print("\nRescaled Dataset (Min-Max Normalization):\n", data_rescaled.head())


### Task b: Standardizing (Transform to Gaussian Distribution) ###
# Initialize the StandardScaler
scaler_standard = StandardScaler()

# Apply StandardScaler to standardize the dataset (excluding the target column 'quality')
data_standardized = pd.DataFrame(scaler_standard.fit_transform(data.iloc[:, :-1]), columns=data.columns[:-1])

# Add the target column back to the standardized data
data_standardized['quality'] = data['quality']

# Display the first 5 rows of the standardized dataset
print("\nStandardized Dataset (Gaussian Distribution):\n", data_standardized.head())


### Task c: Binarizing Data (Thresholding values) ###
# Initialize the Binarizer with a threshold (for example, 0.5)
binarizer = Binarizer(threshold=0.5)

# Apply the Binarizer (excluding the target column 'quality')
data_binarized = pd.DataFrame(binarizer.fit_transform(data.iloc[:, :-1]), columns=data.columns[:-1])

# Add the target column back to the binarized data
data_binarized['quality'] = data['quality']

# Display the first 5 rows of the binarized dataset
print("\nBinarized Dataset (Threshold=0.5):\n", data_binarized.head())
