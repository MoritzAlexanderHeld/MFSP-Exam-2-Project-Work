# Creates the main menu
# 1.    Reads the players.txt file and saves each stored player and
#       highscore in a list
# 2.    If the user selects a player with an already saved name, the
#       stats will update accordingly. If not, it creates the player
# 3.    Sets the computer difficulty in case that's the chosen game style

from player import Player
from intelligence import intelligence
from game import Game


class Menu1:
    def __init__(self):
        self.player_list = []
        self.computer = None

    def get_players(self):
        file = open('players.txt', 'r')
        for line in file:
            line.split(',')
            name = line[0]
            player = Player(name)
            player.highscore.played_games = line[1]
            player.highscore.won_games = line[2]
            player.highscore.average_steps_to_win = line[3]
            self.player_list.append(player)
        file.close()

    def save_players(self):
        file = open('players.txt', 'w')
        for player in self.player_list:
            file.write(f'{player.name},{player.highscore.played_games},{player.highscore.won_games},{player.highscore.average_steps_to_win}')
        file.close()

    def start_menu(self):
        self.get_players()
        print("Welcome to the Pig Dice Game!")
        print("1. Play PvP (Player vs Player)")
        print("2. Play PvC (Player vs Computer)")
        choice = input("Enter choice (1/2): ")

        if choice == '1':       # PvP
            player1 = self.select_player()        # Create Player1
            player2 = self.select_player()        # Create Player2
            game = Game(player1, player2)
            game.turn(player1)
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
                for player in self.player_list:
                    if player.name == name:
                        print("Welcome back, {}!".format(name))
                        self.player_list.remove(player)
                        return player
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
