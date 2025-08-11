"""
13_range.py
-----------
This file covers:
- Range function to generate sequences of numbers
"""

# Using range() in a loop
for i in range(5):  # Generates numbers from 0 to 4
    print(i)

# Using range() with start, stop, and step
for i in range(1, 10, 2):  # Generates numbers from 1 to 9, with a step of 2
    print(i)

# Reverse range
for i in range(10, 0, -1):  # Generates numbers from 10 to 1
    print(i)

# Using range() to create a list
print(list(range(3)))  # Output: [0, 1, 2]
print(list(range(5, 15, 3)))  # Output: [5, 8, 11, 14]

# Nested loops with range
for i in range(3):
    for j in range(1, 6):
        print(f'{i} x {j} = {i * j}')
