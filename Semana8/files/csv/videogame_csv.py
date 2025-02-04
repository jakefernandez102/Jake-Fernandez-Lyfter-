import csv

def main():
    videojuegos = [
      {
        'name': "The Legend of Zelda: Breath of the Wild",
        'genre': "Aventura, Acción, RPG",
        'developers': "Nintendo EPD",
        'esrb_rating': "E10+"
      },
      {
        'name': "Red Dead Redemption 2",
        'genre': "Acción, Mundo Abierto",
        'developers': "Rockstar Games",
        'esrb_rating': "M"
      },
      {
        'name': "God of War (2018)",
        'genre': "Acción, Aventura",
        'developers': "Santa Monica Studio",
        'esrb_rating': "M"
      },
      {
        'name': "Elden Ring",
        'genre': "RPG, Acción",
        'developers': "FromSoftware",
        'esrb_rating': "M"
      },
      {
        'name': "Minecraft",
        'genre': "Sandbox, Supervivencia",
        'developers': "Mojang Studios",
        'esrb_rating': "E10+"
      }
    ];

    video_game_headers = (
      'name',
      'genre',
      'developers',
      'esrb_rating'
    )
    try:
        user_option = input('Do you want to create a new file? (y/n): ')
        if user_option.lower() == 'y':            
            with open('videogame_file.csv','w', encoding='utf-8') as file:
                writer = csv.DictWriter(file,video_game_headers)
                writer.writeheader()
                writer.writerows(videojuegos)
            print('The file has been created successfully')

            user_option = input('Do you want to add new videogame? (y/n): ')
            while user_option.lower() == 'y':
                add_videogame()
                print('The videogame has been added successfully')
                user_option = input('Do you want to add new videogame? (y/n): ')
        else:
            print('Operation canceled')        
    except FileExistsError as ex:
        raise FileExistsError('The file already exists in the directory', ex)
    except FileNotFoundError as ex:
        raise FileNotFoundError('The file was not found in the directory', ex)

def add_videogame():
    videogames = read_videogames()
    print(videogames)
    videogame = fill_videogame()
    videogames.append(videogame)

    try:
        with open('videogame_file.csv','w',encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=videogames[0].keys())
            writer.writeheader()
            writer.writerows(videogames)
    except FileExistsError as ex:
        raise FileExistsError('The file already exists in the directory', ex)
    except FileNotFoundError as ex:
        raise FileNotFoundError('The file was not found in the directory', ex)

def read_videogames():
    try:
        with open('videogame_file.csv','r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            videogames = list(reader)
            print(videogames)
            return videogames
    except FileNotFoundError as ex:
        raise FileNotFoundError('The file was not found in the directory', ex)

def fill_videogame():
    name = input('Name: ')
    genre = input('Genre: ')
    developers = input('Developers: ')
    esrb_rating = input('ESRB Rating: ')
    videogame = {
        'name': name,
        'genre': genre,
        'developers': developers,
        'esrb_rating': esrb_rating
    }
    return videogame

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print('Desde main',ex)


# import csv

# def main():
#     videojuegos = [
#       {
#         'name': "The Legend of Zelda: Breath of the Wild",
#         'genre': "Aventura, Acción, RPG",
#         'developers': "Nintendo EPD",
#         'esrb_rating': "E10+"
#       },
#       {
#         'name': "Red Dead Redemption 2",
#         'genre': "Acción, Mundo Abierto",
#         'developers': "Rockstar Games",
#         'esrb_rating': "M"
#       },
#       {
#         'name': "God of War (2018)",
#         'genre': "Acción, Aventura",
#         'developers': "Santa Monica Studio",
#         'esrb_rating': "M"
#       },
#       {
#         'name': "Elden Ring",
#         'genre': "RPG, Acción",
#         'developers': "FromSoftware",
#         'esrb_rating': "M"
#       },
#       {
#         'name': "Minecraft",
#         'genre': "Sandbox, Supervivencia",
#         'developers': "Mojang Studios",
#         'esrb_rating': "E10+"
#       }
#     ];

#     video_game_headers = (
#       'name',
#       'genre',
#       'developers',
#       'esrb_rating'
#     )
#     try:
#         with open('videogame_file.csv','x', encoding='utf-8') as file:
#             csv.excel_tab.delimiter = ' '
#             writer = csv.DictWriter(file,video_game_headers,dialect='excel-tab')
#             writer.writeheader()
#             writer.writerows(videojuegos)
#         print('The file has been created successfully')
#     except FileExistsError as ex:
#         raise FileExistsError('The file already exists in the directory', ex)
#     except FileNotFoundError as ex:
#         raise FileNotFoundError('The file was not found in the directory', ex)

# if __name__ == '__main__':
#     try:
#         main()
#     except Exception as ex:
#         print('Desde main',ex)