"""
01_map_function.py
-------------------
This file covers:
- Using the map() function to apply a process to a list
"""

# Data
num_list = [1, 2, 3]  # data

# General Method
def update_list(num_list):
    new_list = []
    for i in num_list:
        new_list.append(i + 1)  # process
    return new_list

print(update_list(num_list))  # Process with traditional method

# Using Map
def updater(new_list):
    return new_list + 1  # Adds 1 to each element

print(list(map(updater, [3, 4, 5])))  # Apply 'updater' function using map
