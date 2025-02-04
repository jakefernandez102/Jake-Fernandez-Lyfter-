def main():
    open_file('Hello.txt')
    # write_in_file_as_append('hello.txt', '\nHello World from Python')
    write_in_file_as_write('hello.txt', 'Hello World from Python')
    create_file('hello_created.txt','Hello World from Python')

def open_file(path):
    with open(path) as file:
        print(file.read())

def write_in_file_as_append(path, text):
    with open(path,'a') as file:
        file.write(text)

def write_in_file_as_write(path, text):
    with open(path,'w') as file:
        file.write(text)

def create_file(path,text):
    with open(path,'x') as file:
        file.write(text)

if __name__ == '__main__':
    main()