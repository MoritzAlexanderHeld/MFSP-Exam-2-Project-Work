class player:

    def __init__(self, name, highscore=0):

        self.name = name
        self.highscore = highscore
        self.games_played = 0

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def highscore(self) -> int:
        return self.highscore

    def increment_games_played(self):
        self.games_played += 1

