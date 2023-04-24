# Contains the general structure of the game

from menu1 import Menu1

if __name__ == "__main__":
    menu = Menu1()
    menu.start_menu()
    while True:
        menu.print_menu()
        user_input = input()
        menu.select_option(user_input)
