"""
01_basics.py
---------------
This file covers:
- Printing in Python
- Taking input
- String formatting methods
"""

# Printing Hello World
print("Hello World!")

# Taking user input
name = input("Enter your name: ")
print("Welcome", name)

# String Formatting Methods
name = "Hamamama"
age = 21

# Method 1: format() with placeholders
print("Hello {}, Your age is {}".format(name, age))

# Method 2: format() with index
print("Your age is {1}, {0}".format(name, age))

# Method 3: f-string (Recommended in Python 3.6+)
print(f"Hello {name}, your age is {age}")
