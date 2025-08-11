"""
03_zip_function.py
-------------------
This file covers:
- Using the zip() function to combine multiple iterables
"""

# Data
list_name = ['Khan', 'Ali', 'Jam', 'Jagu']
list_email = ['khan@gmail.com', 'ali@gmail.com', 'jam@gmail.com', 'jagu@gmail.com']
list_numbers = [100, 200, 150, 250, 400]  # last element is ignored due to unequal lengths

# Using zip() to combine lists into tuples
print(list(zip(list_name, list_email, list_numbers)))  # Combine elements of multiple lists
