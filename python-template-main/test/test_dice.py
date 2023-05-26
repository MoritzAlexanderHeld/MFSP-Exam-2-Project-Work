"""testing dice class."""

import sys
import unittest
from unittest.mock import patch
from pigdice.dice import Dice
sys.path.insert(0, '../python-template-main/pigdice')


class DiceTests(unittest.TestCase):
    """in the setUp we create an instance of the dice, to be able to test it."""

    def setUp(self):
        self.dice = Dice()

# Here we test for all possible values, if the expected output is printed
# To do so, we use the patch function of the mock module, which is part of unittest
# The values are hard coded, as it appears to me, it makes sense, to make the tests as
# primitive as possible, to reduce the risk of having mistakes in the tests.
    def test_display(self):
        test_cases = [
            {"dice_value": 1, "expected_output": "╔═════════╗\n║         ║\n║    *    ║\n║         ║\n╚═════════╝"},
            {"dice_value": 2, "expected_output": "╔═════════╗\n║ *       ║\n║         ║\n║       * ║\n╚═════════╝"},
            {"dice_value": 3, "expected_output": "╔═════════╗\n║ *       ║\n║    *    ║\n║       * ║\n╚═════════╝"},
            {"dice_value": 4, "expected_output": "╔═════════╗\n║ *     * ║\n║         ║\n║ *     * ║\n╚═════════╝"},
            {"dice_value": 5, "expected_output": "╔═════════╗\n║ *     * ║\n║    *    ║\n║ *     * ║\n╚═════════╝"},
            {"dice_value": 6, "expected_output": "╔═════════╗\n║ *     * ║\n║ *     * ║\n║ *     * ║\n╚═════════╝"},
        ]

        with patch("builtins.print") as mock_print:
            for test_case in test_cases:
                dice_value = test_case["dice_value"]
                expected_output = test_case["expected_output"]
                self.dice.display(dice_value)
                mock_print.assert_called_with(expected_output)
                mock_print.reset_mock()

# As there are no printed pictures involved
# and the procedure is exactly the same for every value,
# here we only test for two values.
    def test_roll(self):
        with patch("random.randint") as mock_randint:
            mock_randint.return_value = 1  # Here we mock the randint function with the value 1
            result = self.dice.roll()
            self.assertEqual(result, 1)  # assertEqual checks if the actual value is equal to the expected value 1
            mock_randint.assert_called_with(1, 6)  # This checks if the method is called with a valid value(between 1-6)
            mock_randint.reset_mock()  # This clears the mock history, making sure that future tests are not impacted.

# Now the same procedure for the value 3
            mock_randint.return_value = 3
            result = self.dice.roll()
            self.assertEqual(result, 3)
            mock_randint.assert_called_with(1, 6)


if __name__ == "__main__":
    unittest.main()
