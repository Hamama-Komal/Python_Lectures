"""
05_list_comprehension.py
-------------------------
This file covers:
- List comprehension examples for better readability and conciseness
"""

# Old Method to create a list
num_list = []
for i in range(1, 11):
    num_list.append(i)

print(num_list)

# List Comprehension Method
num_list = [i for i in range(1, 11)]  # Expression, loop, and condition in one line
print(num_list)

# List Comprehension with Condition
num_list = [i**2 for i in range(1, 11)]  # Square of numbers
print(num_list)

# List Comprehension with condition (even numbers)
num_list = [i**2 for i in range(1, 11) if i % 2 == 0]  # Square of even numbers
print(num_list)
