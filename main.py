import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ctypes

# Step 1: Generate the Synthetic Dataset
def generate_dataset():
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

# Step 2: Preliminary Data Analysis
def preliminary_analysis():
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

# Step 3: Integrate C++ Library with Python
def integrate_logistic_map():
    # Load the shared library
    lib = ctypes.CDLL('./liblogistic_map.so')

    # Define the logistic_map function
    logistic_map = lib.logistic_map
    logistic_map.argtypes = [ctypes.c_double, ctypes.c_double]
    logistic_map.restype = ctypes.c_double

    # Parameters for the logistic map
    r = 3.9
    x0 = 0.5
    iterations = 1000

    # Generate logistic map data
    x = np.zeros(iterations)
    x[0] = x0

    for i in range(1, iterations):
        x[i] = logistic_map(x[i-1], r)

    # Save the logistic map data using the new graphic processing library
    save_logistic_map_data('./logistic_map_data.csv', x, iterations)

    # Plot the logistic map results
    plt.figure(figsize=(10, 6))
    plt.plot(range(iterations), x, label='Logistic Map')
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title('Logistic Map Demonstrating Non-Linear Dynamics')
    plt.legend()
    plt.show()

def save_logistic_map_data(filename, data, length):
    # Load the graphic processing shared library
    lib_graphic = ctypes.CDLL('./libgraphic_processing.so')

    # Define the save_logistic_map_data function
    save_data = lib_graphic.save_logistic_map_data
    save_data.argtypes = [ctypes.c_char_p, np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), ctypes.c_int]
    save_data.restype = None

    # Call the function to save data
    save_data(filename.encode('utf-8'), data, length)

# Step 4: Data Analysis using C++
def data_analysis():
    # Load the dataset
    data = pd.read_csv('economic_expenditure.csv')
    expenditure = data['expenditure'].values

    # Load the data analysis shared library
    lib_data_analysis = ctypes.CDLL('./libdata_analysis.so')

    # Define the compute_mean and compute_stddev functions
    compute_mean = lib_data_analysis.compute_mean
    compute_mean.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), ctypes.c_int]
    compute_mean.restype = ctypes.c_double

    compute_stddev = lib_data_analysis.compute_stddev
    compute_stddev.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'), ctypes.c_int, ctypes.c_double]
    compute_stddev.restype = ctypes.c_double

    # Calculate mean and standard deviation
    mean = compute_mean(expenditure, len(expenditure))
    stddev = compute_stddev(expenditure, len(expenditure), mean)

    print(f"Mean expenditure: {mean}")
    print(f"Standard deviation of expenditure: {stddev}")

# Step 5: Non-Linear Dynamic Model
def non_linear_dynamic_model():
    # Load the shared library
    lib_non_linear = ctypes.CDLL('./libnon_linear_model.so')

    # Define the non_linear_dynamic function
    non_linear_dynamic = lib_non_linear.non_linear_dynamic
    non_linear_dynamic.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
    non_linear_dynamic.restype = ctypes.c_double

    # Parameters for the non-linear model
    r = 3.9
    b = 0.1
    x0 = 0.5
    iterations = 1000

    # Generate non-linear dynamic model data
    x = np.zeros(iterations)
    x[0] = x0

    for i in range(1, iterations):
        x[i] = non_linear_dynamic(x[i-1], r, b)

    # Plot the non-linear dynamic model results
    plt.figure(figsize=(10, 6))
    plt.plot(range(iterations), x, label='Non-Linear Dynamic Model')
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title('Non-Linear Dynamic Model with Reduced Space Complexity')
    plt.legend()
    plt.show()

# Run the steps in order
if __name__ == "__main__":
    generate_dataset()
    preliminary_analysis()
    integrate_logistic_map()
    data_analysis()
    non_linear_dynamic_model()
