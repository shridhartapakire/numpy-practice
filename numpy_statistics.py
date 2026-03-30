# NumPy Day 4 - Random, Statistics & Useful Functions

import numpy as np

# 1. Random numbers
rand_arr = np.random.rand(5)
print("Random values:", rand_arr)

rand_int = np.random.randint(1, 10, size=5)
print("\nRandom integers:", rand_int)

# 2. Statistics
data = np.array([10, 20, 30, 40, 50])

print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Sum:", np.sum(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

# 3. Sorting
unsorted = np.array([5, 2, 9, 1, 7])
sorted_arr = np.sort(unsorted)

print("\nUnsorted:", unsorted)
print("Sorted:", sorted_arr)

# 4. Unique values
arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_vals = np.unique(arr)

print("\nUnique values:", unique_vals)

# 5. Conditional filtering
nums = np.array([10, 25, 30, 45, 50])
filtered = nums[nums > 30]

print("\nValues > 30:", filtered)