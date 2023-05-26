"""tests player class."""
import unittest
from pigdice.player import Player


class TestPlayer(unittest.TestCase):

    """Creating an instance of player "John""""
    def setUp(self):
        self.player = Player("John")

    # Testing if the name was set correctly
    def test_get_name(self):
        self.assertEqual(self.player.get_name(), "John")

    # Testing if the score for a new player is 0, obviously a new player shouldn't have a score yet.
    # This is not connected to the high score. The high score saves how many turns a player needed to win.
    # This saves the points the player has in the game.
    def test_get_score(self):
        self.assertEqual(self.player.get_score(), 0)

    # Repeating the same test for the total score
    def test_get_total_score(self):
        self.assertEqual(self.player.get_total_score(), 0)

    # This checks if the turns are also set to 0 for a new player.
    def test_get_turns(self):
        self.assertEqual(self.player.get_turns(), 0)

    # This checks if the player is correctly set up as human
    def test_is_human(self):
        self.assertTrue(self.player.is_human())

    # This tests the total score again, after setting it to 100
    def test_set_total_score(self):
        self.player.set_total_score(100)
        self.assertEqual(self.player.get_total_score(), 100)

    # This tests the turns after setting them to 5
    def test_set_turns(self):
        self.player.set_turns(5)
        self.assertEqual(self.player.get_turns(), 5)

    # Checks if the player is not set as winner, which should be the case under 100 points
    def test_is_not_winner(self):
        self.assertTrue(self.player.is_not_winner())

    # Checks if the counter for played turns is increased by 1, when the method is called
    def test_add_turn(self):
        self.player.add_turn()
        self.assertEqual(self.player.get_turns(), 1)

    # Checks if the score is reset properly by calling the reset_score method
    # and then calling get_score and checking if the value is 0
    def test_reset_score(self):
        self.player.reset_score()
        self.assertEqual(self.player.get_score(), 0)

    # Test the add score method in the same way as above, but adding 5
    def test_add_score(self):
        self.player.add_score(5)
        self.assertEqual(self.player.get_score(), 5)

    # Checks if the total score is updated correctly, by first increasing the current score,
    # then updating the total score and then checking if it holds the correct value
    def test_update_total_score(self):
        self.player.add_score(10)
        self.player.update_total_score()
        self.assertEqual(self.player.get_total_score(), 10)

    # Checks if the name is changed properly, by calling the change_name method with a new name as argument
    # and then checking if the get_name method returns the new name.
    def test_change_name(self):
        self.player.change_name("Mike")
        self.assertEqual(self.player.get_name(), "Mike")


if __name__ == '__main__':
    unittest.main()
