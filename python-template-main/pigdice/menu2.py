# Creates the secondary menu, stating the player data

# The rules of the game are missing

from highscore import Highscore
from menu1 import Menu1


class Menu2:
    def __init__(self, player):  # Here every integer is assigned the associated menu point.
        self.player = player
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
            highscore.display_high_scores()
        elif option == "2":
            # print("You selected Change Name")
            name = input("New name: ")
            self.player.set_name(name)
        elif option == "3":
            # print("You selected Display Rules")
            self.display_rules()
        elif option == "4":
            # print("You selected Restart and will be brought to the start menu.")
            menu_1 = Menu1()
            menu_1.start_menu()
        elif option == "5":
            exit()

    def display_rules():
        print("")
