import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./liblogistic_map.so')

# Define the logistic_map function
logistic_map = lib.logistic_map
logistic_map.argtypes = [ctypes.c_double, ctypes.c_double]
logistic_map.restype = ctypes.c_double

# Parameters
r = 3.9
x0 = 0.5
iterations = 1000

# Generate logistic map data
x = np.zeros(iterations)
x[0] = x0

for i in range(1, iterations):
    x[i] = logistic_map(x[i-1], r)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(iterations), x, label='Logistic Map')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Logistic Map Demonstrating Non-Linear Dynamics')
plt.legend()
plt.show()
