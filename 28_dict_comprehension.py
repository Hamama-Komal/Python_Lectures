"""
07_dict_comprehension.py
-------------------------
This file covers:
- Dictionary comprehension to create dictionaries concisely
"""

# Original dictionary
my_dic = {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension to square values
update_dic = {key: value**2 for key, value in my_dic.items()}
print(update_dic)  # Creates a new dictionary with squared values
