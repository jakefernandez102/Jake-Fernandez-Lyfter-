from menu.menu import menu
def main():
    print("Welcome to our school system! \n\n")

    menu()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f'Error in general Exception: {ex}')
        exit(1)
