import json

def main():
    data= []
    try:
        while True:
            with open('pokemons.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for pokemon in data:
                  print(pokemon)

            print("Hello, welcome to the Pokemon database!")
            user_pokemon = get_user_pokemon()
            print(user_pokemon)
            data.append(user_pokemon)

            with open('pokemons.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            if(input("Do you want to add another Pokemon? (y/n): ") == 'n'):
                break

    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except KeyError:
        print("Error: Key not found in JSON data.")

def get_user_pokemon():
    pokemon_name = input("Enter the name of the Pokemon in english: ")
    pokemon_types = get_pokemon_types()
    pokemon_base = get_pokemon_base()
    

    return {
        'name':{
            'english': pokemon_name
            } ,
        'type': pokemon_types,
        'base': pokemon_base
    }
    

def get_pokemon_types():
    pokemon_types = []
    while True:
        pokemon_type = input("Enter the type of the Pokemon: ")
        pokemon_types.append(pokemon_type)
        if(input("Do you want to add another type? (y/n): ") == 'n'):
            break
    return pokemon_types

def get_pokemon_base():
    base = {}
    try:
        base['HP'] = int(input("Enter the HP of the Pokemon: "))
        base['Attack'] = int(input("Enter the Attack of the Pokemon: "))
        base['Defense'] = int(input("Enter the Defense of the Pokemon: "))
        base['Sp. Atk'] = int(input("Enter the Sp. Atk of the Pokemon: "))
        base['Sp. Def'] = int(input("Enter the Sp. Def of the Pokemon: "))
        base['Speed'] = int(input("Enter the Speed of the Pokemon: "))
    except ValueError as ex:
        raise ValueError("Error: Invalid value for base stats it must be number values.") from ex
    return base

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')