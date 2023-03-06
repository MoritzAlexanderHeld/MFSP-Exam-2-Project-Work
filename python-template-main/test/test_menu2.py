import unittest
from pigdice.menu2 import Menu_2
import io                                  # This and the following module is necessary to put the printed menu into a buffer
from contextlib import redirect_stdout     # and compare it as string to the expected output.

class TestMenu2(unittest.TestCase):
    def test_print_menu(self):
        menu2 = Menu_2()
        with io.StringIO() as buf, redirect_stdout(buf):  # Here the printed output is redirected to the buffer.
            menu2.print_menu()
            printed_output = buf.getvalue()               # Here the content of the buffer is assigned to a variable as string.
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

# Here the content of the buffer is compared to the expected output. Still does not work.
        self.assertEqual(expected_output, printed_output)

# ------------------------------------------------------------------------------------------------------------------------------
#    def test_select_option(self):
        