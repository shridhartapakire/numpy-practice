# NumPy Day 1 - Basics

import numpy as np

# 1. Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 2. Array properties
print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data type:", arr2.dtype)

# 3. Special arrays
zeros = np.zeros((2, 3))
print("\nZeros Array:\n", zeros)

ones = np.ones((2, 2))
print("\nOnes Array:\n", ones)

# 4. Range array
range_arr = np.arange(0, 10, 2)
print("\nRange Array:", range_arr)

# 5. Linspace
linspace_arr = np.linspace(0, 1, 5)
print("\nLinspace Array:", linspace_arr)