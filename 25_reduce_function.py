"""
04_reduce_function.py
----------------------
This file covers:
- Using the reduce() function to combine data together
"""

from functools import reduce

# Data
num_list = [1, 2, 3, 3, 4, 4, 5]

# Function to combine data
def combiner(bucket, no_list):
    return bucket + no_list

# Using reduce() to accumulate the sum
print(reduce(combiner, num_list, 0))  # Combine elements using the combiner function
