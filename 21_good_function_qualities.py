"""
07_good_function_qualities.py
------------------------------
This file covers:
- Good qualities of well-written functions
"""

# Good Function Qualities
# 1) Always returns the expected output
# 2) Have no side effects on the rest of the code
# 3) Function names must be meaningful and related
# 4) Well-organized and easy to understand

# Example of a good function:
def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

# The function is simple, has a meaningful name, and does exactly what it says
print(add_numbers(5, 3))  # Returns 8
