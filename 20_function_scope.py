"""
06_function_scope.py
---------------------
This file covers:
- Scope of variables in functions
- Local, non-local, global variables
"""

# Example of function scope (variable 'num' is local)
def scope_testing():
    num = 10  # Local variable

# print(num)  # Will give an error because 'num' is local to the function

# Accessing different scopes
text = "Global Scope"

def function():
    text = "Non Local Scope"  # Non-local variable
    def nested_function():
        global text  # Access global variable 'text'
        return text
    return nested_function()

print(function())  # Outputs "Global Scope"
