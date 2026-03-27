# NumPy Day 2 - Array Operations & Indexing

import numpy as np

# 1. Create array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# 2. Indexing
print("\nFirst element:", arr[0])
print("Last element:", arr[-1])

# 3. Slicing
print("\nSlice [1:4]:", arr[1:4])
print("Every second element:", arr[::2])

# 4. 2D Array Indexing
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

print("Element at (1,2):", arr2[1, 2])

# 5. Mathematical Operations
print("\nAdd 10:", arr + 10)
print("Multiply by 2:", arr * 2)

# 6. Array to Array operations
arrA = np.array([1, 2, 3])
arrB = np.array([4, 5, 6])

print("\nAddition:", arrA + arrB)
print("Multiplication:", arrA * arrB)