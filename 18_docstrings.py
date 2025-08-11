"""
04_docstrings.py
----------------
This file covers:
- Adding docstrings for function documentation
"""

def return_fun(a, b):
    ''' This function adds two integers and returns their sum. '''
    sum = a + b
    return sum

help(return_fun)  # Displays the docstring of the function
