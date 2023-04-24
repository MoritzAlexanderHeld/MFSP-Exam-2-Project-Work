from dice import Dice
#from dicehand import DiceHand
from game import game
#from player import player


class intelligence:
    game = game([])
    print(game.players[0].dicehand.turn_score)
    
    def computer_play(self):
        
        if self.difficulty == "easy":
            while game.players[1].dicehand.turn_score < 20:
                roll = Dice.roll()
                if roll == 1:
                    print("Computer rolled a 1 and lost its turn.")
                    return
                else:
                    game.players[1].score += roll
                    print(f"Computer rolled a {roll}. Current score: {game.players[1].dicehand.score}")
                    
                    
                    """
                    
        if dice_value == 1:
            print("Computer rolled a 1 and lost its turn.")
            return
        else:
            self.players[1].play()
    
        if self.players[1].score > 20:
            print("Computer ends its turn.")
            return
        if dice_value == 1:
            print("Computer rolled a 1 and lost its turn.")
            return
        else:
            self.players[1].play()
            
 
        while self.players[1].score < 30:
            if dice_value == 1:
                print("Computer rolled a 1 and lost its turn.")
                return
            else:
                self.players[1].play()"""