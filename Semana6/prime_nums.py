# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*


def get_prime_numbers(number_list = []):
    is_prime = False
    prime_list = []

    if(len(number_list) == 0):
      return 'List is empty'
    
    for number in number_list:
      is_prime = validate_prime_number(number)
      if(is_prime):
          prime_list.append(number)
    return prime_list


def validate_prime_number(number):
    if number <= 1:
        return False
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


print(get_prime_numbers([2,7,4,3,10,19]))
