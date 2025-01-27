###
# 03 - Lists.
###

import os

os.system("clear")

# Example of a list in Python
fruits: list[str] = ["apple", "banana", "cherry"]
numbers: list[int] = [1, 2, 3, 4, 5]
numbers_and_fruits = [1, 2, 3, 4, 5, "apple", "banana", "cherry"] 
empty_list: list = []
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a list
print(fruits[1]) # banana
print(fruits[-1]) # cherry
print(fruits[-2]) # banana
print(matrix[1][1]) # 5

# Slicing a list
print(fruits[:2]) # ['apple', 'banana']
print(fruits[1:]) # ['banana', 'cherry']
print(fruits[1:2]) # ['banana']
print(fruits[-2:]) # ['banana', 'cherry']
print(fruits[:]) # ['apple', 'banana', 'cherry'] hace una copia de la lista

print(fruits[::2]) # ['apple', 'cherry'] salta de 2 en 2
print(fruits[::-1]) # ['cherry', 'banana', 'apple'] invierte la lista

# Modifying elements in a list
fruits[1] = "blackberry"
print(fruits) # ['apple', 'blackberry', 'cherry']
# fruits[33] = "orange" # IndexError: list assignment index out of range

# Adding elements to a list
fruits = fruits + ["grape", "pear"]
print(fruits) # ['apple', 'blackberry', 'cherry', 'grape', 'pear']

print(len(fruits)) # 9


