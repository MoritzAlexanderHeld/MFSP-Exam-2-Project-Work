from player import player
"""import dice
import dicehand
import highscore
import intelligence
import menu1
import menu2"""


class Game:
    def __init__(self, players=[]):
        self.players = players
        self.players.append(player("Reem", 0))
        self.players.append(player("Computer"))
        
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