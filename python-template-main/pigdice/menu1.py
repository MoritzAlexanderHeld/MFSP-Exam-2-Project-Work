# Creates the main menu, creates players and sets the computer difficulty in
# case that's the chosen game style

from player import Player
from intelligence import intelligence


class Menu1:
    def __init__(self):
        self.player_list = []
        self.computer = None

    def get_players(self):
        file = open('players.txt', 'r')
        for line in file:
            line.split(',')
            name = line[0]
            played_games = line[1]
            won_games = line[2]
            average_steps_to_win = line[3]
            player = Player(name)
            player.highscore.set_highscore(played_games, won_games, average_steps_to_win)

    def start_menu(self):
        print("Welcome to the Pig Dice Game!")
        print("1. Play PvP (Player vs Player)")
        print("2. Play PvC (Player vs Computer)")
        choice = input("Enter choice (1/2): ")

        if choice == '1':       # PvP
            self.select_player()        # Create Player1
            self.select_player()        # Create Player2
            # code for PvP game

        elif choice == '2':     # PvC
            self.select_player()        # Create Player1
            self.select_difficulty()    # Create Computer
            # code for PvC game

    def create_player(self):
        name = input("Enter your name: ")
        new_player = Player(name)
        self.player_list.append(new_player)
        print("Welcome, {}! Your player profile has been created.".format(name))

    def select_player(self):
        while True:
            is_new_player = input("Are you a new player? (y/n): ")
            if is_new_player.lower() == 'n':
                name = input("Enter your name: ")
                if name in self.player_list:
                    print("Welcome back, {}!".format(name))
                else:
                    print("No player with that name exists.")
                    create_new = input("Do you want to create a new player? (y/n): ")
                    if create_new.lower() == 'y':
                        self.create_player()
                    else:
                        print("Exiting game.")
                        exit()
                return
            elif is_new_player.lower() == 'y':
                self.create_player()
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def select_difficulty(self):
        return
