
def main():
    song_list = []
    with open('song_names.txt') as file:
        song_name = file.read()
        song_list =(song_name.split('\n'))
    sorted_song_list = sort_alfabetically(song_list)

    with open('song_names.txt', 'w') as file:
        for song in sorted_song_list:
            file.write(song + '\n')

def sort_alfabetically(song_list=[]):
    try:
        sorted_titles = sorted(song_list, key=lambda x: x.split('. ', 1)[1])
        return sorted_titles
    except IndexError:
        raise IndexError('The song list is empty')

if __name__ == '__main__':
    try:
        main()
    except IndexError as ex:
        print(ex)