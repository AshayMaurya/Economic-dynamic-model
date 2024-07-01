import numpy as np
import pandas as pd

# Set a seed for reproducibility
np.random.seed(42)

# Generate time series data
time = np.arange(100)

# Generate synthetic expenditure data with a trend and some noise
expenditure = np.cumsum(np.random.randn(100)) + 50

# Create a DataFrame
data = pd.DataFrame({
    'time': time,
    'expenditure': expenditure
})

# Save the dataset to a CSV file
data.to_csv('economic_expenditure.csv', index=False)

print("Dataset created and saved as 'economic_expenditure.csv'")
