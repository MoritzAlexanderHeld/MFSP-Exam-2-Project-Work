class Player:
 
    def __init__(self, name, score=0, total_score=0, turns=0, human=True):
        self.name = name
        self.score = score
        self.total_score = total_score
        self.turns = turns
        self.human = human

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_total_score(self):
        return self.total_score

    def get_turns(self):
        return self.turns

    def is_human(self):
        return self.human

    def set_total_score(self, total_score):
        self.total_score = total_score

    def set_turns(self, turns):
        self.turns = turns

    def is_not_winner(self):
        return (self.total_score + self.score) < 100

    def add_turn(self):
        self.turns += 1

    def reset_score(self):
        self.score = 0

    def add_score(self, dice_value):
        self.score += dice_value

    def update_total_score(self):
        self.total_score += self.score

    def change_name(self, name):
        self.name = name
