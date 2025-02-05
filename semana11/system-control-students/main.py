from menu.Menu import Menu
def main():
    print("Welcome to our school system! \n\n")
    menu= Menu()
    menu.display_menu()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f'Error in general Exception: {ex}')
        exit(1)
