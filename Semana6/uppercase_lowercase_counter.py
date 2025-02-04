# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def uppercase_lowercase_counter(string=''):
    uppercase_counter =0
    lowercase_counter =0

    for char in string:
          if(char.isupper()):
              uppercase_counter += 1
          else:
              lowercase_counter +=1
    return f'There are {uppercase_counter} upper cases and {lowercase_counter} lower cases'

print(uppercase_lowercase_counter('I love Nación Sushi'))
