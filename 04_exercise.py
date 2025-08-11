"""
04_exercise.py
---------------
This file covers:
- Exercise for getting user input
- Reversing a string as an encryption/decryption example
"""

# Get input from user and encrypt it for security
user_name = input('Enter Your Name: ')[::-1]  # reverse the user entered name >> Encode
print(f"Encrypted Name: {user_name}")

# Decrypt by reversing the string
print(f"Decrypted Name: {user_name[::-1]}")
