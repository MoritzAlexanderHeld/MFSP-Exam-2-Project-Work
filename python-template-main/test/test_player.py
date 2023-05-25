import unittest
from pigdice.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("John")

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), "John")

    def test_get_score(self):
        self.assertEqual(self.player.get_score(), 0)

    def test_get_total_score(self):
        self.assertEqual(self.player.get_total_score(), 0)

    def test_get_turns(self):
        self.assertEqual(self.player.get_turns(), 0)

    def test_is_human(self):
        self.assertTrue(self.player.is_human())

    def test_set_total_score(self):
        self.player.set_total_score(100)
        self.assertEqual(self.player.get_total_score(), 100)

    def test_set_turns(self):
        self.player.set_turns(5)
        self.assertEqual(self.player.get_turns(), 5)

    def test_is_not_winner(self):
        self.assertTrue(self.player.is_not_winner())

    def test_add_turn(self):
        self.player.add_turn()
        self.assertEqual(self.player.get_turns(), 1)

    def test_reset_score(self):
        self.player.reset_score()
        self.assertEqual(self.player.get_score(), 0)

    def test_add_score(self):
        self.player.add_score(5)
        self.assertEqual(self.player.get_score(), 5)

    def test_update_total_score(self):
        self.player.add_score(10)
        self.player.update_total_score()
        self.assertEqual(self.player.get_total_score(), 10)

    def test_change_name(self):
        self.player.change_name("Mike")
        self.assertEqual(self.player.get_name(), "Mike")


if __name__ == '__main__':
    unittest.main()
