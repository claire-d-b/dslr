import numpy as np
from statistics import ft_statistics

# Define the data
data = [434, 34, 562, 73, 121, 9, 8, 67, 322]
data2 = [34, 3, 62, 730, 11, 0, 67, 6]

# Sort the data
sorted_data = sorted(data)

# Calculate quartiles using numpy
Q1 = np.percentile(sorted_data, 25)
Q3 = np.percentile(sorted_data, 75)

# Print results
print("First Quartile (Q1):", Q1)
print("Third Quartile (Q3):", Q3)

# Sort the data
sorted_data2 = sorted(data2)

# Calculate quartiles using numpy
Q1 = np.percentile(sorted_data2, 25)
Q3 = np.percentile(sorted_data2, 75)

# Print results
print("First Quartile (Q1):", Q1)
print("Third Quartile (Q3):", Q3)

ft_statistics(434, 34, 562, 73, 121, 9, 8, 67, 322, toto="quartile")
ft_statistics(34, 3, 62, 730, 11, 0, 67, 6, toto="quartile")
