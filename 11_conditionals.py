"""
11_conditionals.py
-------------------
This file covers:
- if, elif, else statements
- Logical operators: `or`, `and`
- Identity operators: `is`, `is not`
"""

# if - elif - else
cat = False
owner = True

if cat:
    print("Mouse is killed by cat")
elif owner:
    print("Mouse ran away")
else:
    print("Mouse ate cheese")

# 'or' and 'and' Logical Operators
if True or False:
    print('True or False: or gives True')
if True or True:
    print('True or True: or gives True')
if False or False:
    print('False or False: or gives False')

if True and False:
    print('True and False: and gives False')
if True and True:
    print('True and True: and gives True')
if False and False:
    print('False and False: and gives False')

# Identity Operators: Compare memory location
num1 = 1
num2 = 1

# 'is' checks if both variables point to the same memory location
print(num1 is num2)  # True because both point to the same location

print([1, 2, 3] is [1, 2, 3])  # False because lists are different objects in memory
print([1, 2, 3] is not [1, 2, 3])  # True because lists are different objects
