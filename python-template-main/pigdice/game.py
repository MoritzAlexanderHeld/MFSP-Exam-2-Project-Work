from player import Player
from dicehand import DiceHand
"""import dice
import dicehand
import highscore
import intelligence
import menu1
import menu2"""


class Game:
    def __init__(self, player1, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.menu_options = {
            "1": "Roll",
            "2": "Hold",
            "3": "Settings"
        }

    def print_menu(self):  # This prints the menu. The 5 options dynamic to allow changes and make it less hard coded.
        print("*----------------*")
        for option, description in self.menu_options.items():
            print(f"| {option}. {description:<12}|")
        print("*----------------*")
        self.select_option()

    def select_option(self):
        option = input()
        while option not in self.menu_options:
            print("Invalid input, try again.")
            option = input()
        if option == "1":
            dice_value = dice_hand.
            highscore.display_high_scores()
        elif option == "2":
            # print("You selected Change Name")
            name = input("New name: ")
            self.player.set_name(name)
        elif option == "3":
            # print("You selected Display Rules")
            self.display_rules()

    def turn(self, player):
        player.dice
        
        """
        self.high_scores = update_stats()


num_turns = 0

        
def start(self):
    print("Welcome to Pig Dice!")
    num_players = int(input("How many players? "))
    for i in range(num_players):
        name = input(f"Enter the name for player {i+1}: ")
        self.players.append(Player(name))
    self.difficulty = input("Enter difficulty level (easy/medium/hard): ")

    while True:
        for player in self.players:
            print(f"\n{player.name}'s turn")
            player.play()
            if player.score >= 100:
                self.end_game(player)
                return
        self.computer_play()
        
"""