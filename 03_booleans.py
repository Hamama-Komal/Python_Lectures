"""
03_booleans.py
---------------
This file covers:
- Boolean values
- Truthy and falsy values in Python
"""

# Boolean Values
my_boolean_value = True  # Boolean has 2 values: True or False
print(my_boolean_value)

# Truthy and Falsy Examples
print(bool(0))  # bool treats 0 as False
print(bool(-3))  # any non-zero number is considered True
print(bool(12))  # non-zero is True
print(bool(1))  # non-zero is True

print(bool('Hello'))  # if there is any string, it returns True
print(bool(''))  # empty string returns False
