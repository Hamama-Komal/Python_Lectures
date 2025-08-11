"""
14_loop_controls.py
---------------------
This file covers:
- break, continue, and pass keywords in loops
"""

# Using 'break' to exit a loop
for i in range(10):
    print(i)
    if i == 5:
        break  # Exit the loop when i is 5

# Using 'continue' to skip the current iteration
for i in range(10):
    if i == 5:
        continue  # Skip the iteration when i is 5
    print(i)  # This will print all values except 5

# Using 'pass' to do nothing (placeholder)
for i in range(5):
    if i == 3:
        pass  # Pass does nothing, allows the loop to continue
    print(i)  # This will print all values, including 3, but with no action taken when i is 3
