# NumPy Day 6 - Practice Problems

import numpy as np

# 1. Create array and find sum
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Sum:", np.sum(arr))

# 2. Find mean and max
print("\nMean:", np.mean(arr))
print("Max:", np.max(arr))

# 3. Filter values greater than 25
filtered = arr[arr > 25]
print("\nValues > 25:", filtered)

# 4. Create 2D array and reshape
arr2 = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr2.reshape(2, 3)
print("\nReshaped:\n", reshaped)

# 5. Add two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nAddition:", a + b)

# 6. Multiply array by scalar
print("Multiply by 3:", arr * 3)

# 7. Generate random integers
rand = np.random.randint(1, 50, size=5)
print("\nRandom integers:", rand)

# 8. Sort array
unsorted = np.array([9, 3, 7, 1, 5])
print("\nSorted:", np.sort(unsorted))