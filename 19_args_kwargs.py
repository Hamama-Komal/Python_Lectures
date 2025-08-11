"""
05_args_kwargs.py
-----------------
This file covers:
- Using *args and **kwargs to handle multiple arguments
"""

# Using *args to handle an arbitrary number of positional arguments
def adder(*args):
    return sum(args)

print(adder(1, 2, 3, 4, 5))  # Sum of all arguments

# Using **kwargs to handle keyword arguments
def adder(*args, **kwargs):
    print(kwargs)  # Print all keyword arguments
    return sum(args)

print(adder(1, 2, 3, price=50, amount=60))
