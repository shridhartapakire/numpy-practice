# NumPy Day 5 - Broadcasting & Advanced Operations

import numpy as np

# 1. Broadcasting with scalar
arr = np.array([1, 2, 3])
print("Original:", arr)

result = arr + 5
print("\nAdd scalar (5):", result)

# 2. Broadcasting with arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

print("\nArray 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)

# 3. 2D Broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

print("\nMatrix:\n", matrix)
print("Vector:", vector)

print("Matrix + Vector:\n", matrix + vector)

# 4. Advanced operations
arr3 = np.array([1, 4, 9, 16])

print("\nSquare root:", np.sqrt(arr3))
print("Exponential:", np.exp(arr3))
print("Logarithm:", np.log(arr3))

# 5. Comparison operations
nums = np.array([10, 20, 30, 40])

print("\nGreater than 20:", nums > 20)
print("Filtered values:", nums[nums > 20])