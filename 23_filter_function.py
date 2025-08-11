"""
02_filter_function.py
----------------------
This file covers:
- Using the filter() function to filter data based on a condition
"""

# Filter: Filters data according to a given process (returns only even numbers)
def separator(num_list):
    return num_list % 2 == 0

# Using filter() to get even numbers
print(list(filter(separator, [1, 4, 3, 5, 6, 8])))  # Filters out odd numbers
