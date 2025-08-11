"""
09_tuples.py
-------------
This file covers:
- Tuple creation, access, and immutability
- Common tuple methods
"""

# Tuple: Ordered, Immutable
my_tuple = (1, 2, 3)
print(my_tuple)

# Accessing Tuple Elements
print(my_tuple[1])  # Access tuple item by index

# Immutability of Tuple
# my_tuple[1] = 4  # Will give error: 'tuple' object does not support item assignment

# Tuple Unpacking
a, b, c = my_tuple  # Unpacking values into variables
print(a, b, c, sep="     ")

# Tuple Methods
new_tuple = (1, 23, 44, 1, 1, 34, 24, 44)
print(len(new_tuple))  # Get the length of the tuple
print(22 in new_tuple)  # Check if an element exists in tuple
print(new_tuple.count(1))  # Count occurrences of the value '1'
print(new_tuple.index(44))  # Get the index of the value '44'
