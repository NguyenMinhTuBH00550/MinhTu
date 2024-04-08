import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read data from the 'dirty_data.csv' file
df = pd.read_csv('dirty_data.csv')

# Drop previously created fake columns
df = df.drop(columns=[f'fake_column_{i}' for i in range(1, 21)])

# Remove duplicate rows
df = df.drop_duplicates()

# Remove columns with all null values
df = df.dropna(axis=1, how='all')

# Split the data into features and target
X = df.drop(columns=['Address'])  # Replace 'target_column' with the actual target column name
y = df['Address']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Identify categorical columns for one-hot encoding
categorical_cols = [col for col in X_train.columns if X_train[col].dtype == 'object']




# Create a transformer for one-hot encoding
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(), categorical_cols)],
    remainder='passthrough'
)

# Initialize the RandomForestClassifier model
model = RandomForestClassifier()

# Save the cleaned DataFrame to a new file
df.to_csv('cleaned_data.csv', index=False)
