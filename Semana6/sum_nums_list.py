# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

def sum_nums(num_list):
  total=0
  for number in num_list:
    total += number
  return total

print(sum_nums([1,2,4,5]))
print(sum_nums([1,2]))
print(sum_nums([2,4]))