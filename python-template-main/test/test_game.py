import sys
sys.path.insert(0, '../python-template-main/pigdice')
import unittest
from unittest.mock import patch
import game
from player import Player


class GameTestCase(unittest.TestCase):

    def test_select_starting_player(self):
        players = ["Player1", "Player2"]
        starting_player = game.select_starting_player(players)
        self.assertIn(starting_player, players)

    def test_update_current_player(self):
        players = ["Player1", "Player2"]
        current_player = players[0]
        new_current_player = game.update_current_player(players, current_player)
        self.assertEqual(new_current_player, players[1])

    def test_cheat(self):
        player = Player("Player1", False)
        with patch("builtins.input", side_effect=['1', '100']):
            game.cheat(player)
            self.assertEqual(player.get_total_score(), 100)

        with patch("builtins.input", side_effect=['2', '5']):
            game.cheat(player)
            self.assertEqual(player.get_turns(), 5)

    def test_play_game(self):
        players = [Player("Player1", True), Player("Player2", False)]
        with patch("builtins.input", side_effect=['r', 'h']):
            with patch("game.Dice.roll", return_value=3):       # THE PROBLEM IS HERE
                # with patch("game.display_scores"):
                players[0].set_total_score(20)
                players[1].set_total_score(10)
                game.play_game(players, 1)
                self.assertEqual(players[0].get_total_score(), 20)


if __name__ == '__main__':
    unittest.main()