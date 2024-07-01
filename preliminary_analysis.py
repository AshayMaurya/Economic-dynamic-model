import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('economic_expenditure.csv')

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['expenditure'], label='Expenditure')
plt.xlabel('Time')
plt.ylabel('Expenditure')
plt.title('Economic Expenditure Over Time')
plt.legend()
plt.show()
