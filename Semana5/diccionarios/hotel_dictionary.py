# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#     - `nombre`
#     - `numero_de_estrellas`
#     - `habitaciones`
# - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#     - `numero`
#     - `piso`
#     - `precio_por_noche`

hotel ={}

hotel_name= input('Ingrese el nombre del hotel')
hotel_stars= input('Ingrese el numero de estrellas del hotel')
hotel_rooms= []

hotel['name']= hotel_name
hotel['stars']= hotel_stars
hotel['rooms']= hotel_rooms

finish_inserting_rooms = False
while(finish_inserting_rooms != True):
    room_number = input('Ingrese el numero de habitacion:')
    room_floor = input('Ingrese el piso de la habitacion')
    room_price = input('Ingrese el precio por noche de la habitacion')

    add_room = input('Desea agregar otra habitacion? Si/No')

    while(add_room != 'si' and add_room != 'no' and add_room != 'Si' and add_room != 'No' and add_room != 'SI' and add_room != 'NO'):
        add_room = input('Desea agregar otra habitacion? Si/No')

    if(add_room == 'si' or add_room == 'Si' or add_room == 'SI'):
        finish_inserting_rooms= False
    elif(add_room == 'no' or add_room == 'No' or add_room == 'NO'):
        finish_inserting_rooms= True

    hotel_room={'number':room_number,'floor':room_floor,'price':room_price}

    hotel['rooms'].append(hotel_room)


print(hotel)