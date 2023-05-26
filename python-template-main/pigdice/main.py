from pigdice.highscore import Highscore
from pigdice.player import Player
import game


# Formats and prints the game rules
def display_rules():
    print("""\n\n===== Rules =====
\tOne player rolls the die, if a 1 is rolled, the turn is lost, otherwise \
the rolled value is
\tadded to the turn score. The player must decide when to hold, at that \
time the turn score
\tis added to the total score. No points are scored when a 1 is rolled.
\tThe first player to reach 100 points wins.
\t\tPress [N] to change the player's name
\t\tPress [X] to exit the current game""")
    input()


# Function to prompt for the difficulty level of the computer player
def get_computer_difficulty():
    print("Difficulty\n1. Easy\n2. Normal\n3. Hard")
    while True:
        try:
            difficulty = int(input("Enter the difficulty level of the computer (1-3): "))
            if 1 <= difficulty <= 3:
                return difficulty
            else:
                print("Invalid difficulty level. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Main menu
def main_menu():
    highscore = Highscore()
    while True:
        print("\n===== PIG DICE GAME =====")
        print("[1] Player vs Player")
        print("[2] Player vs Computer")
        print("[3] High Scores")
        print("[4] Rules")
        print("[5] Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            player1_name = input("Player 1. Enter your name: ")
            player2_name = input("Player 2. Enter your name: ")
            players = [
                Player(player1_name),
                Player(player2_name)
            ]
            game.play_game(players, 0)
        elif choice == '2':
            player_name = input("Enter your name: ")
            players = [
                Player(player_name),
                Player("Computer", human=False)
            ]
            computer_difficulty = get_computer_difficulty()
            game.play_game(players, computer_difficulty)
        elif choice == '3':
            highscore.display_high_scores()
        elif choice == '4':
            display_rules()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Start the game
if __name__ == '__main__':
    main_menu()
