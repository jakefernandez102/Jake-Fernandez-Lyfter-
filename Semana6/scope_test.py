# 2. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor.

def creating_variable_inside_function():
  FUNCTION_VARIABLE='I belong to creating_variable_inside_function function'

print(FUNCTION_VARIABLE)

GLOBAL_VARIABLE='I am a global variable';

def access_to_global_variable():
  print(GLOBAL_VARIABLE)