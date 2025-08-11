"""
08_dictionaries.py
-------------------
This file covers:
- Dictionary creation and basic operations
- Common dictionary methods
"""

# Dictionary: Unordered, Mutable, Key-Value Pairs
my_dic = {'key1': [1, 2, 3, 5], 'key2': 'Hello', 'key3': 123, 'key4': 12.678, 'key5': False}
print(my_dic['key5'])  # Access dictionary by key
print(my_dic['key1'][3])  # Access item in list within dictionary

# Testing keys with different data types
testing_keys = {1: "Hello", "2": "Hii", 3.3: "False", False: True}
print(testing_keys[1], testing_keys['2'], testing_keys[3.3], testing_keys[False])

# Common Methods of Dictionary
print(my_dic.items())  # Prints all key-value pairs in tuple form
print(my_dic.keys())   # Prints all the keys of the dictionary
print(my_dic.values())  # Prints all the values of the dictionary
print(my_dic.get('key6'))  # Using get() to avoid errors if key is not found (returns None)

# Checking existence of a key or value
print('key5' in my_dic.keys())  # Checks if 'key5' exists in keys
print('123' in my_dic.values())  # Checks if '123' exists in values

# Removing items from dictionary
print(my_dic.popitem())  # Removes and returns the last key-value pair
print(my_dic)
