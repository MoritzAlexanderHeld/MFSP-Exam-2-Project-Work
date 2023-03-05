import unittest
from pigdice.menu2 import Menu_2

class TestMenu2(unittest.TestCase):
    def test_display_menu(self):
        menu2 = Menu_2()
        menu2.print_menu()
        expected_output = """*----------------*
|      MENU      |
|----------------|
| 1. Highscore   |
| 2. Change name |
| 3. View rules  |
| 4. Restart     |
| 5. Exit        |
|----------------|"""

# The current problem is that a string (expected_output is compared to an object.
# To use this method I have to pass the string that the object prints instead.
# Simply doing str(menu2) does not work, neither does "menu2.print_menu()"
        self.assertEqual(expected_output, menu2.print_menu())
