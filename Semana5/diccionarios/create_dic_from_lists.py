# 1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#     1. Ejemplos:
#     2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#     `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#     → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

composed_dictionary ={}

for index in range(0, len(list_a)):
  composed_dictionary[list_a[index]]=list_b[index]

print(composed_dictionary)