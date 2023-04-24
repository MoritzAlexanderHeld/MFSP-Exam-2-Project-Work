# Keeps track of the games played, won and the scored points in each play,
# and displays all that data


class Highscore:
    def __init__(self):
        self.played_games = 0
        self.won_games = 0
        self.average_steps_to_win = 0
        self.diceHand_list = []

    def set_highscore(self, played_games, won_games, average_steps_to_win):
        self.played_games = played_games
        self.won_games = won_games
        self.average_steps_to_win = average_steps_to_win

    def update_stats(self, won, diceHand_score):
        self.played_games += 1
        if won:
            self.won_games += 1
            self.diceHand_list.append(diceHand_score)

    def display_high_scores(self):
        winning_rate = self.won_games / self.played_games if self.played_games > 0 else 0
        self.average_steps_to_win = (self.average_steps_to_win * self.won_games + (sum(self.diceHand_list) / len(self.diceHand_list))) / (self.won_games + 1) if self.diceHand_list else self.average_steps_to_win
        display_string = "Played games: {}, Won games: {}, Winning rate: {:.2f}, Average steps to win: {:.2f}".format(self.played_games, self.won_games, winning_rate, self.average_steps_to_win)
        return display_string
