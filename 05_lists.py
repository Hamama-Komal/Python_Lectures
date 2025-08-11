"""
05_lists.py
---------------
This file covers:
- List indexing, slicing, and methods
- Nested lists and list manipulation
"""

# List Operations
list_1 = [1, 2, 3, 4, 5]  # Don't use list as variable name as it is a keyword.
print(list_1)

list_2 = ['abc', 'cde', 'fgh', 'ijk']
print(list_2[2])  # Access list item by index number

# List with mixed data types
mix_list = [ 1, 3.4, 'Hello', True]  # List can contain values of different data types
print(mix_list[2])

# List in List (Nested List)
list_in_list = [1, 2, 3, ['a', 'b', 'c', 'd'], 4, 5, [3.4, 9.7, 3.4]]  
print(list_in_list[3])  # Access inner list
print(list_in_list[6][1])  # Access item in nested list

# List Slicing and Reversal
# [starting_point: ending_point: step]
print(list_in_list[1:3])  # Slicing: start at index 1 and end at index 2
print(list_in_list[::-1])  # Reverse the list
print(list_in_list[:])  # Print the whole list
print(list_in_list[1:5:2])  # Slicing with step 2

# Modifying Lists
list_in_list[2] = "Hello"  # Can modify lists because they are mutable
print(list_in_list)

# Built-in List Functions
list_in_list.insert(3, "Hey")  # Insert at index 3
print(list_in_list)

list_in_list.append("Good Bye")  # Append to the end of the list
print(list_in_list)

list_in_list.remove("Hello")  # Remove specific item
print(list_in_list)

print(list_in_list.pop())  # Pop the last item from the list
print(list_in_list.pop(3))  # Pop the item at index 3

list_in_list.extend("hey")  # Add elements of a string into the list as separate items
print(list_in_list)

list_in_list.clear()  # Clear the list
print(list_in_list)

# Other List Operations
list_1.reverse()  # Reverse the list
print(list_1)

list_1.sort()  # Sort the list
print(list_1)

print(list_1.index(4))  # Return the index of the given value

# Counting Elements
list_1.append(1)
list_1.append(1)
list_1.append(2)
list_1.append(1)
print(list_1)
print(list_1.count(1))  # Count how many times the value 1 appears

# Using range() to generate lists
print(list(range(1, 100)))  # Generate a list from 1 to 99

# Unpacking Lists into Variables
a, b, c, *d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)  # First element
print(b)  # Second element
print(c)  # Third element
print(d)  # Remaining elements
