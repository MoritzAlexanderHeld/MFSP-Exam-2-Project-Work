"""creates dice object."""
import random


class Dice:
    """creatig dice ASCII art."""
    def __init__(self):
        self.dice_art = [
            "╔═════════╗\n║         ║\n║    *    ║\n║         ║\n╚═════════╝",
            "╔═════════╗\n║ *       ║\n║         ║\n║       * ║\n╚═════════╝",
            "╔═════════╗\n║ *       ║\n║    *    ║\n║       * ║\n╚═════════╝",
            "╔═════════╗\n║ *     * ║\n║         ║\n║ *     * ║\n╚═════════╝",
            "╔═════════╗\n║ *     * ║\n║    *    ║\n║ *     * ║\n╚═════════╝",
            "╔═════════╗\n║ *     * ║\n║ *     * ║\n║ *     * ║\n╚═════════╝"
        ]

    def display(self, dice_value):
        print(self.dice_art[dice_value - 1])

    def roll(self):
        return random.randint(1, 6)
