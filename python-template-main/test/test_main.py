
import sys
sys.path.insert(0, '../python-template-main/pigdice')
import unittest
from unittest.mock import patch
from io import StringIO
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.players = [
            main.Player("Player1"),
            main.Player("Player2")
        ]

    def test_display_rules(self):
        # Redirect stdout to capture the output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.display_rules()
            output = fake_out.getvalue().strip()
            expected_output = "===== Rules =====\n\tOne player rolls the die, if a 1 is rolled, the turn is lost, otherwise the rolled value is\n\tadded to the turn score. The player must decide when to hold, at that time the turn score\n\tis added to the total score. No points are scored when a 1 is rolled.\n\tThe first player to reach 100 points wins.\n\t\tPress [N] to change the player's name\n\t\tPress [X] to exit the current game"
            self.assertEqual(output, expected_output)

    def test_get_computer_difficulty_valid(self):
        # Mock the input function to return a valid difficulty level
        with patch('builtins.input', return_value='2'):
            difficulty = main.get_computer_difficulty()
            self.assertEqual(difficulty, 2)

    def test_get_computer_difficulty_invalid_then_valid(self):
        # Mock the input function to return an invalid difficulty level first, then a valid one
        with patch('builtins.input', side_effect=['5', '3']):
            # Redirect stdout to capture the output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                difficulty = main.get_computer_difficulty()
                output = fake_out.getvalue().strip()
                expected_output = "Invalid difficulty level. Please enter a number between 1 and 3."
                self.assertEqual(difficulty, 3)
                self.assertEqual(output, expected_output)

    def test_main_menu_choice_1(self):
        # Mock the input function to simulate user input
        with patch('builtins.input', side_effect=['1', 'Player1', 'Player2']):
            # Mock the game.play_game function to check if it's called with the correct arguments
            with patch('main.game.play_game') as mock_play_game:
                main.main_menu()
                mock_play_game.assert_called_with(self.players, 0)

    def test_main_menu_choice_2(self):
        # Mock the input function to simulate user input
        with patch('builtins.input', side_effect=['2', 'Player1', '2']):
            # Mock the game.play_game function to check if it's called with the correct arguments
            with patch('main.game.play_game') as mock_play_game:
                # Mock the get_computer_difficulty function to return the correct value
                with patch('main.get_computer_difficulty', return_value=2):
                    main.main_menu()
                    mock_play_game.assert_called_with(self.players, 2)

    # Add more tests for the remaining choices in the main_menu function


if __name__ == '__main__':
    unittest.main()
