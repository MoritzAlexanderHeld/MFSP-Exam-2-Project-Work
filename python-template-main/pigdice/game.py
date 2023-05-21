import random

from player import Player
from dice import Dice


# Prints the banner celebrating the winner
def print_weener():
    print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄                ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌              ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌              ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌              ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌              ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌              ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌              ▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌              ▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌          ▐░▌     ▐░▌  
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌              ▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌              ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
      """)


# Function to update the high score file (high score = minimum number of turns necessary to win a game)
def update_high_scores(player_name, game_turns):
    high_scores = {}
    try:
        # Read the high score file
        with open("high_scores.txt", "r") as file:
            for line in file:
                name, turns = line.strip().split(",")
                high_scores[name] = int(turns)
    except FileNotFoundError:
        pass

    # Update the high score for the player or add a new entry
    if player_name in high_scores:
        if high_scores[player_name] > int(game_turns):
            high_scores[player_name] = int(game_turns)
    else:
        high_scores[player_name] = int(game_turns)

    # Write the updated high scores to the file
    with open("high_scores.txt", "w") as file:
        for name, turns in high_scores.items():
            file.write(f"{name},{turns}\n")


# Function to display the high score record
def display_high_scores():
    high_scores = {}
    try:
        # Read the high score file
        with open("high_scores.txt", "r") as file:
            for line in file:
                name, turn = line.strip().split(",")
                high_scores[name] = int(turn)

        # Sort the high scores by the least number of rounds
        sorted_scores = sorted(high_scores.items(), key=lambda x: x[1])

        # Display the high score record
        print("\nHigh Scores:")
        print("-" * 13)
        for i, (name, turn) in enumerate(sorted_scores, start=1):
            print(f"{i}. {name}: {turn} rounds")

    except FileNotFoundError:
        print("No high scores available.")


# Function to display the current scores
def display_scores(players):
    print("Current Scores:")
    print("-" * 15)
    for player in players:
        print(f"{player.get_name()}: {player.get_score()} points (Total: {player.get_total_score()} points)")
    print("\n" + "-" * 15 + "\n")


# Function to determine the winner
def determine_winner(players):
    winner = max(players, key=lambda x: x['total_score'])
    print_weener()
    print(f"\n{winner['name']} wins with a score of {winner['total_score']} points!")


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


# Function to select a random player to start the game
def select_starting_player(players):
    return players[random.randint(0, 1)]


# Function to update the current player
def update_current_player(players, current_player):
    if players.index(current_player) == 0:
        return players[1]
    else:
        return players[0]


# Function to play the game
def play_game(players, computer_difficulty):
    current_player = select_starting_player(players)
    print(f"\nLet's begin the game! {current_player.get_name()} starts.\n")

    dice = Dice()

    while True:
        display_scores(players)

        # Player's turn
        if current_player.is_human():
            print(f"{current_player.get_name()}, it's your turn.")
            player_choice = input(f"\n{current_player.get_name()}, choose [r]oll or [h]old: ").lower()

            if player_choice == 'r':
                dice_value = dice.roll()
                dice.display(dice_value)
                if dice_value == 1:
                    current_player.add_turn()
                    print("Oops! You rolled a 1. Your turn is over, and you scored nothing.")
                    current_player.reset_score()
                    current_player = update_current_player(players, current_player)
                else:
                    print(f"You rolled a {dice_value}!")
                    current_player.add_score(dice_value)
            elif player_choice == 'h':
                current_player.add_turn()
                current_player.update_total_score()
                current_player.reset_score()
                if current_player.is_winner():
                    break
                current_player = update_current_player(players, current_player)
            elif player_choice == "n":
                name = input("Write your NEW name: ")
                current_player.change_name(name)
            elif player_choice == "x":
                return
            elif player_choice == "cheat":
                cheat()
            else:
                print("Invalid choice. Please enter a valid character")

        # Computer's turn
        else:
            print(f"{current_player.get_name()}'s turn (Difficulty: {computer_difficulty})")

            # Select the strategy based on the difficulty level
            if computer_difficulty == 1:
                if current_player.get_score() < 20:
                    player_choice = 'r'
                else:
                    player_choice = 'h'
            elif computer_difficulty == 2:
                turns_remaining = (100 - current_player.get_total_score()) // current_player.get_score()
                if turns_remaining > 4:
                    target_score = 25
                else:
                    target_score = (100 - current_player.get_total_score()) // turns_remaining
                if current_player.get_score() < target_score:
                    player_choice = 'r'
                else:
                    player_choice = 'h'
            elif computer_difficulty == 3:
                if current_player.get_total_score() < 71:
                    target_score = 21 + (71 - current_player.get_total_score()) // 8
                else:
                    target_score = 100 - current_player.get_total_score()
                if current_player.get_score() < target_score:
                    player_choice = 'r'
                else:
                    player_choice = 'h'

            if player_choice == 'r':
                input("The computer decided to roll")
                dice_value = dice.roll()
                dice.display(dice_value)
                if dice_value == 1:
                    print("Oops! The computer rolled a 1. Its turn is over, and it scored nothing.")
                    current_player.reset_score()
                    current_player = update_current_player(players, current_player)
                else:
                    print(f"The computer rolled a {dice_value}!")
                    current_player.add_score(dice_value)
            elif player_choice == 'h':
                input("The computer decided to hold")
                current_player.update_total_score()
                current_player.reset_score()
                if current_player.is_winner():
                    break
                current_player = update_current_player(players, current_player)

    # Game ends, determine the weener and update high scores
    print_weener()
    print(f"\n{current_player.get_name()} wins with a score of {current_player.get_total_score()} points!")
    if current_player.is_human():
        update_high_scores(current_player.get_name(), current_player.get_turns())


# Cheat code
def cheat():
    print("What would you like to change?")

# Main menu
def main_menu():
    while True:
        print("\n===== PIG DICE GAME =====")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. High Scores")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            player1_name = input("Player 1. Enter your name: ")
            player2_name = input("Player 2. Enter your name: ")
            players = [
                Player(player1_name),
                Player(player2_name)
            ]
            play_game(players, 0)
        elif choice == '2':
            player_name = input("Enter your name: ")
            players = [
                Player(player_name),
                Player("Computer", human=False)
            ]
            computer_difficulty = get_computer_difficulty()
            play_game(players, computer_difficulty)
        elif choice == '3':
            display_high_scores()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Start the game
if __name__ == '__main__':
    main_menu()
