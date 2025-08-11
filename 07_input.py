"""
07_input.py
------------
This file covers:
- Using input() to get user input
- Demonstrating how input() treats the input as string by default
"""

# Get input from user
name = input('Enter Your Name: ')
age = input('Enter your age: ')

# Output user input
print(name, age, sep=" & ", end="\n")  # Separate the values by "&" and end with a newline
print(type(name), type(age), sep=" & ",)  # Check the data types of the input values
