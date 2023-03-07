import unittest

from pigdice.player import player


class TestPlayer(unittest.TestCase):
    
    # def setup(self):
    #     self.P1 = player("John", 50)
     
    def test_player_attributes(self):
        # Create a new player and check its attributes
        p1 = player("John", 50)
        self.assertEqual(p1.name, "John")
        self.assertEqual(p1.highscore, 50)
        self.assertEqual(p1.games_played, 0)

    def test_name_setter(self):
        # Create a new player and change its name
        p1 = player("John")
        p1.set_name("Jane")
        self.assertEqual(p1.get_name, "Jane")
        p1.set_name("mike")
        self.assertEqual(p1.get_name, "mike")

    def test_increment_games_played(self):
        # Create a new player and increment the games played
        p1 = player("John")
        p1.increment_games_played()
        self.assertEqual(p1.games_played, 1)


if __name__ == '__main__':    
    unittest.main()
