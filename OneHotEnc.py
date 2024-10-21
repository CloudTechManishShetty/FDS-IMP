import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
data = pd.read_csv('Data.csv')

# Task a: Apply OneHot encoding on the 'Country' column
onehotencoder = OneHotEncoder(sparse=False)
country_encoded = onehotencoder.fit_transform(data[['Country']])

# Create a DataFrame from the OneHot encoded data
country_encoded_df = pd.DataFrame(country_encoded, columns=onehotencoder.get_feature_names_out(['Country']))

# Concatenate the OneHot encoded columns with the original DataFrame (dropping the 'Country' column)
data = pd.concat([data.drop('Country', axis=1), country_encoded_df], axis=1)

# Task b: Apply Label encoding on the 'Purchased' column
labelencoder = LabelEncoder()
data['Purchased'] = labelencoder.fit_transform(data['Purchased'])

# Print the transformed dataset
print("Transformed Dataset:")
print(data)
