# NumPy Day 3 - Reshaping, Stacking, Splitting

import numpy as np

# 1. Reshaping
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print("Original:", arr)
print("\nReshaped (2x3):\n", reshaped)

# 2. Flattening
flat = reshaped.flatten()
print("\nFlattened:", flat)

# 3. Vertical Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstack = np.vstack((a, b))
print("\nVertical Stack:\n", vstack)

# 4. Horizontal Stacking
hstack = np.hstack((a, b))
print("\nHorizontal Stack:", hstack)

# 5. Splitting arrays
arr2 = np.array([1, 2, 3, 4, 5, 6])

split = np.split(arr2, 3)
print("\nSplit into 3 parts:", split)