import unittest
from unittest.mock import patch
import pigdice.game
from pigdice.player import Player


class GameTestCase(unittest.TestCase):

    # Checks if a player is randomly picked to start the game
    # To do so we create a list with two players, call the select_starting_player method
    # and assign the returned value to the variable "starting_player" and then check if
    # the value of starting_player is in the list
    def test_select_starting_player(self):
        players = ["Player1", "Player2"]
        starting_player = pigdice.game.select_starting_player(players)
        self.assertIn(starting_player, players)

    # Tests if the current player is updated correctly by creating a list of two players again,
    # then first assigning Player1 to the variable current_player and then calling the method,
    # which should read which player is currently assigned to current_player and assign the other one
    # to "new_current_player"
    # Then we check if new_current_player holds players[1] (Player2)
    def test_update_current_player(self):
        players = ["Player1", "Player2"]
        current_player = players[0]
        new_current_player = pigdice.game.update_current_player(players, current_player)
        self.assertEqual(new_current_player, players[1])

    # Here we test the cheat function by setting up a non-human player,
    # patching the inputs 1 (to choose the option "Total score")
    # and 100 (to set the score to 100) and then checks if the new total score is equal to 100
    # We might have to change the value to 99, in case we run into issues because 100 terminates the game.
    def test_cheat(self):
        player = Player("Player1", False)
        with patch("builtins.input", side_effect=['1', '100']):
            pigdice.game.cheat(player)
            self.assertEqual(player.get_total_score(), 100)

    # Here we repeat the procedure, but instead of changing the total score,
    # we patch the inputs 2 and 5, to change the turns to 5.
        with patch("builtins.input", side_effect=['2', '5']):
            pigdice.game.cheat(player)
            self.assertEqual(player.get_turns(), 5)

    # Here we test the play_game function. We first set up two player, one human and one not human.
    # Then we patch the inputs 'r' and 'h' to roll once and hold once
    # we then patch the roll function with the returned value 3
    def test_play_game(self):
       players = [Player("Player1", True), Player("Player2", False)]
    with patch("builtins.input", side_effect=['r', 'h']):
            with patch("game.Dice.roll", return_value=3):       # THE PROBLEM IS HERE
                # with patch("game.display_scores"):
                players[0].set_total_score(20)
                players[1].set_total_score(10)
                pigdice.game.play_game(players, 1)
                self.assertEqual(players[0].get_total_score(), 20)


if __name__ == '__main__':
    unittest.main()
