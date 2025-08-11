"""
12_loops.py
------------
This file covers:
- For loop
- While loop
- Nested loops
"""

# For Loop: Iterating over a list
fruit_list = ['apple', 'banana', 'grapes', 'oranges']
for fruit in fruit_list:
    print(fruit)

# Nested For Loop: Iterating over two lists
price_list = [100, 200, 300, 400, 500]
for fruit in fruit_list:
    for price in price_list:
        print(f"{fruit} costs {price}")

# While Loop: Runs as long as the condition is true
num = 2
while num < 10:
    print(f'num is {num}')
    num += 1
else:
    print(f'Loop ended as num reached {num}')

# Infinite While Loop with break
num = 0
while True:
    num += 1
    print(num)
    if num == 5:
        break  # Break the loop when num reaches 5
