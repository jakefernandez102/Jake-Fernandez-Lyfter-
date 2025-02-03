# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def reversed_string(input_string):
    reversed_str=''
    for char in range((len(input_string)-1),-1,-1):
        reversed_str += input_string[char]
    return reversed_str

print(reversed_string('Hello World'))
print(reversed_string('Jake Fernandez'))
print(reversed_string('Escriba lo que quiera'))