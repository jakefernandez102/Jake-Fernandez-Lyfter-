# 1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

  

def print_second(string):
  print(string)

def print_first(string):
  print_second(f'{string} ')

def main():
  print_first('Hello')
  print_second('World')

main()