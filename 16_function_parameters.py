"""
02_function_parameters.py
---------------------------
This file covers:
- Parameters and Arguments
- Positional, Default, and Keyword arguments
"""

# Positional Parameters
def positional_fun(name, age):
    print(f'Hello! {name}, your age is {age}')

# Positional Arguments (must match parameter order)
positional_fun("Komal", 24)
positional_fun(18, 'Hamza')  # Incorrect order, can cause issues

# Default Parameters
def default_fun(name="John", age=10):
    print(f'Hello! {name}, your age is {age}')

default_fun("Komal", 24)
default_fun()  # Uses default values if no arguments are passed

# Keyword Parameters
def keyword_fun(name, age):
    print(f'Hello! {name}, your age is {age}')

# Arguments passed as keywords (order doesn't matter)
keyword_fun(name='Hamza', age=10)
keyword_fun(age=30, name='Asif')
