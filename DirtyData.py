import pandas as pd
import numpy as np

# Read data from CSV file
df = pd.read_csv('data.csv')

# Create 20 fake columns
for i in range(1, 21):
    df[f'fake_column_{i}'] = ['fake_data'] * len(df)

# Find the positions of NULL values created
null_indices = np.where(pd.isnull(df))
# Rename 20 randomly chosen values to 'NULL'
num_renamed_values = 20
for _ in range(num_renamed_values):
    row_idx = np.random.randint(0, len(df))  # Randomly choose a row
    col_idx = np.random.randint(0, len(df.columns))  # Randomly choose a column
    if (row_idx, col_idx) not in zip(*null_indices):  # Check if the chosen position is not NULL
        df.iloc[row_idx, col_idx] = 'NULL'  # Set the value to 'NULL'
# Set randomly 10 cells to have no value
for _ in range(10):
    row_idx = np.random.randint(0, len(df))  # Randomly choose a row
    col_idx = np.random.randint(0, len(df.columns))  # Randomly choose a column
    df.iloc[row_idx, col_idx] = np.nan  # Set the value to NaN (no value)
# Add 30 duplicated rows
df = pd.concat([df] * 30, ignore_index=True)
# Save the dirty DataFrame to a new file
df.to_csv('dirty_data.csv', index=False)
