"""
02_strings.py
---------------
This file covers:
- String indexing and slicing
- String immutability
- Common string methods and functions
"""

# String Indexing and Slicing
value = "HELLO WORLD!"
print(value[4])  # print value at index 4
print(value[3:8])  # print the string values from index 3 to 7
print(value[0::1])  # print the value from 0 to end with skip of one value 
print(value[-5]) # use negative indexing to revert the string
print(value[::-1]) # use to revert the string

# String Immutability
name = 'Hamama'
print(name)
print(name[4])
# name[4] = 'Z'  # Not applicable in String
name = 'Komal'  # We can update the whole string with new value
print(name)

# Built-In String Functions
my_string = "Never Give Up."
print(my_string.capitalize())  # Capitalize the 1st letter
print(my_string.endswith('Hehe'))  # Return Boolean if the end value matches or not
print(my_string.upper()) # Convert to upper case
print(my_string.lower()) # Convert to lower case
print(my_string.replace('Never', 'Always')) # Replace the given word
print(my_string) # Original string is unchanged because strings are immutable
print(my_string.find('U')) # Return the index number of the given character
