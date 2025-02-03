# 5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#     1. Ejemplos:
#     2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

COUNTER = 0
number_list = []
max_number = -99999

while COUNTER < 10: 
    number = int(input('Ingrese un número: '))
    number_list.append(number) 
    if max_number < number:
        max_number = number
    COUNTER += 1

print(f'La lista es {number_list} y el número más alto ingresado es: {max_number}')
