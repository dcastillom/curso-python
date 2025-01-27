###
# 04 - Lists methods.
###

import os

os.system("clear")

# Create a sample list
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("After append:", my_list) # [1, 2, 3, 4, 5, 6]

# Extend the list with another list
my_list.extend([7, 8, 9])
print("After extend:", my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert an element at a specific position
my_list.insert(0, 0)
print("After insert:", my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove an element from the list
my_list.remove(3)
print("After remove:", my_list) # [0, 1, 2, 4, 5, 6, 7, 8, 9]

# Pop an element from the list
popped_element = my_list.pop()
print("After pop:", my_list) # [0, 1, 2, 4, 5, 6, 7, 8]
print("Popped element:", popped_element) # 9

# Find the index of an element
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4) # 3

# Count the occurrences of an element
count_of_2 = my_list.count(2) # 1
print("Count of 2:", count_of_2) # 1

# Sort the list
my_list.sort()  # By default, it sorts in ascending order
print("After sort:", my_list) # [0, 1, 2, 4, 5, 6, 7, 8]

# Reverse the list
my_list.reverse()
print("After reverse:", my_list) # [8, 7, 6, 5, 4, 2, 1, 0]


# Eliminar el último elemento de la lista
# lo elimina y lo devuelve
e = my_list.pop()
print(e) # 0
print(my_list) # [8, 7, 6, 5, 4, 2, 1]

# Clear the list
my_list.clear()
print("After clear:", my_list) # []

# Eliminar un range de elementos
my_list = [1, 2, 3, 4, 5]
del my_list[1:3] # Elimina los elementos en el rango [1, 3)
print(my_list) # [1, 4, 5]


# Diferencia entre sort y sorted

# Crear una lista de ejemplo
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Usar sorted() para ordenar la lista sin modificar la lista original
sorted_list = sorted(my_list)
print("Original list:", my_list) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Sorted list:", sorted_list) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Usar sort() para ordenar la lista y modificar la lista original
my_list.sort()
print("List after sort():", my_list) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Sort the list ignoring case
my_list = ['banana', 'Apple', 'cherry', 'apple', 'Banana', 'Cherry']
my_list.sort(key= str.lower)
print("List after case-insensitive sort:", my_list) # ['Apple', 'apple', 'banana', 'Banana', 'cherry', 'Cherry']
