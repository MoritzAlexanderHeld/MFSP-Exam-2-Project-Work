import unittest
from unittest.mock import patch
from pigdice.menu2 import Menu_2

class TestMenu2(unittest.TestCase):
    @patch("builtins.print")
    def test_display_menu(self, mock_print):
        menu = Menu_2()
        menu.print_menu()
        expected_output = """*----------------*
|      MENU      |
|----------------|
| 1. Highscore   |
| 2. Change name |
| 3. View rules  |
| 4. Restart     |
| 5. Exit        |
|----------------|
"""
        mock_print.assert_called_once_with(expected_output)
