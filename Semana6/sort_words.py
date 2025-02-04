# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_words(string):
    sorted_list= create_sorted_list(string)
    sorted_string = convert_sorted_list_to_sorted_string(sorted_list)
    return sorted_string

def create_sorted_list(string):
    word_list = []
    word = ''
    for char in string:
        if(char == ' '):
            return 'Invalid separator, it must be a "-", try again'
        elif(char != '-'):
            word += char
        else:
            print(word)
            word_list.append(word)
            word=''
    word_list.append(word)
    word_list.sort()

    return word_list

def convert_sorted_list_to_sorted_string(sorted_list):
    sorted_string=''
    for index, word in enumerate(sorted_list):
        if(index != len(sorted_list)-1):
            sorted_string += f'{word}-'
        else:
            sorted_string += f'{word}'
    return sorted_string


print(sort_words('jake-steve-fernandez-brizuela'))
