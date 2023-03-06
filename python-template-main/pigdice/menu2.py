class Menu_2:
    def __init__(self):  # Here every integer is assigned the associated menu point.
        self.menu_options = {
            "1": "Highscore",
            "2": "Change name",
            "3": "View rules",
            "4": "Restart",
            "5": "Exit"
        }

    def print_menu(self):  # This prints the menu. The 5 options dynamic to allow changes and make it less hard coded.
        print("*----------------*")
        print("|      MENU      |")
        print("|----------------|")
        for option, description in self.menu_options.items():
            print(f"| {option}. {description:<12}|")
        print("|----------------|")

    def select_option(self, option):
        while option not in self.menu_options:
            print("Invalid input, try again.")
            option = input()

    # The print statements below are there to test on the go.
        if option == "1":
            # print("You selcted Highscore")
            highscore = Highscore()
            highscore.display_highscore()
        elif option == "2":
            # print("You selected Change Name")
            change_name = ChangeName()
            change_name.change_player_name()
        elif option == "3":
            # print("You selected Display Rules")
            rules = Rules()
            rules.display_rules()
        elif option == "4":
            # print("You selected Restart and will be brought to the start menu.")
            menu_1 = Menu()
            menu_1.display_menu()
            menu_1.select_option(input("Select an option: "))
        elif option == "5":
            exit()

if __name__ == "__main__":
    menu = Menu_2()
    while True:
        menu.print_menu()
        user_input = input()
        menu.select_option(user_input)
