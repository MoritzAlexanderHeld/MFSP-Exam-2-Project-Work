# Stores the name and highscore associeted with the player

from dicehand import DiceHand
from dice import Dice
from highscore import Highscore


class Player:

    def __init__(self, name):
        self.name = name
        self.highscore = Highscore()
        self.dicehand = DiceHand()

    def set_name(self, value):
        self.name = value

    def get_name(self):
        return self.name

    def increment_games_played(self):
        self.highscore.player_stats["played_games"] += 1

    def play(self):
        roll = Dice.roll(self)
        if roll == 1:
            print(f"{self.name} rolled a 1 and lost their turn.")
            return
        self.score += roll
        print(f"{self.name} rolled a {roll}. Current score: {self.score}")

    def print_score(self):
        high_scores = self.highscore.display_high_scores()
        print(f"{self.name}: {high_scores}")
