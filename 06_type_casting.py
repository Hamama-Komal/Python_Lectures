"""
06_type_casting.py
--------------------
This file covers:
- Explicit and Implicit type casting in Python
"""

# Explicit Type Casting (manually changing type)
num_string = '123'
num_int = 13
sum = num_int + int(num_string)  # Converting num_string to integer
print('Sum:', sum)
print(type(sum))  # Checking the type of the result

# Implicit Type Casting (automatically changing type)
num_float = 2.34
num_int = 14
sum_num = num_int + num_float  # Python automatically converts num_int to float
print('Sum:', sum_num)
print(type(sum_num))  # Checking the type of the result
