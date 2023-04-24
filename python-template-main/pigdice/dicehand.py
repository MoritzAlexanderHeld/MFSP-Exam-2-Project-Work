# Keeps track of each turn

from dice import Dice


class DiceHand:
    def __init__(self):
        self.score = 0
        self.last_roll = 0

    def roll_dice(self):
        self.last_roll = Dice.roll()
        self.score += self.last_roll
        return self.last_roll

    def print_last_roll(self):
        print(f"Last roll: {self.last_roll}")

    def print_score(self):
        print(f"Current round sum: {self.score}")
