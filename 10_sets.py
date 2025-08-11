"""
10_sets.py
-----------
This file covers:
- Set creation and operations
- Common set methods
"""

# Sets: Unordered, Holds Unique Values
my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

# Sets do not support indexing
# print(my_set[3])  # This will give an error

# Creating a set with duplicate values (duplicates will be removed)
testing_set = {1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 10}
print(testing_set)  # Duplicate values are removed

# Set Methods

my_set.add(100)  # Add an element to the set
print(my_set)

# Union of two sets
print(my_set.union(testing_set))

# Intersection of two sets (common elements)
print(my_set.intersection(testing_set))

# Difference between two sets
print(my_set.difference(testing_set))

# Difference in reverse order
print(testing_set.difference(my_set))
