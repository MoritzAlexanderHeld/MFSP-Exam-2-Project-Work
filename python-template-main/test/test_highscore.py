import sys
sys.path.insert(0, '../python-template-main/pigdice')
import unittest
from io import StringIO
from unittest.mock import patch
from pigdice.highscore import Highscore


class HighscoreTestCase(unittest.TestCase):

    def setUp(self):
        # Here we create an instance again, to be able to perform the tests
        self.highscore = Highscore()
        # We also create a test file, to isolate the test from the actual high_scores.txt
        self.highscore.filename = "test_high_scores.txt"

    def tearDown(self):
        # Here we empty the file, to avoid issues when the test is performed multiple times
        with open(self.highscore.filename, "w") as file:
            file.write("")

    # Now we test the update_high_scores method, by first entering a highscore 10 and then 5
    # (in this case, even though it is called HIGHscore, lower is better)
    # Therefore it is expected that the score of 10 is replaced by the value 5.
    # With this we test two things in one test: If a highscore can be set and if it can be overwritten
    def test_update_high_scores(self):
        self.highscore.update_high_scores("Player1", 10)
        self.highscore.update_high_scores("Player1", 5)

    # Here we open the file for reading
        with open(self.highscore.filename, "r") as file:
            lines = file.readlines()
    # And here we check if PLayer1 is saved with the highscore value 5.
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0], "Player1,5\n")

    def test_display_high_scores(self):
        # First we make sure that the file is empty again
        with open(self.highscore.filename, "w") as file:
            file.write("")
        # Now we write three players to the file
        # To check if they are sorted correctly, they must not be sorted by score yet.
        with open(self.highscore.filename, "w") as file:
            file.write("Reem,10\n")
            file.write("Mo,15\n")
            file.write("Mikael,8\n")

        # Here we redirect the output, so it is not printed, but instead saved in a buffer, where it can be read from
        output = StringIO()
        with patch("sys.stdout", new=output):
            self.highscore.display_high_scores()

        # Here we get the output from above and split it into single lines
        # We tried to compare the output in one step, but ran from one error into the next,
        # so we chose this less elegant way.
        printed_output = output.getvalue().strip().split("\n")

        # Here the lines are compared to the expected output
        self.assertEqual(printed_output[0], "High Scores:")
        self.assertEqual(printed_output[1], "-" * 13)
        self.assertEqual(printed_output[2], "1. Mikael: 8 rounds")
        self.assertEqual(printed_output[3], "2. Reem: 10 rounds")
        self.assertEqual(printed_output[4], "3. Mo: 15 rounds")

    def test_display_high_scores_no_file(self):
        # And again, we make sure the file is empty
        with open(self.highscore.filename, "w") as file:
            file.write("")
        # And again, we redirect the output, to save it in a buffer instead of printing it.
        output = StringIO()
        with patch("sys.stdout", new=output):
            self.highscore.display_high_scores()


if __name__ == '__main__':
    unittest.main()
