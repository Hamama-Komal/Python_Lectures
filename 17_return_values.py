"""
03_return_values.py
--------------------
This file covers:
- Using the `return` keyword in functions
"""

def return_fun(a, b):
    sum = a + b
    return sum  # Function returns the sum

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
print(f'Sum of {num1} & {num2} is {return_fun(num1, num2)}')
