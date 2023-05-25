import random
from pigdice.dice import Dice
from pigdice.highscore import Highscore


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


# Prints the banner shaming the looser (Only in Player Vs Computer mode)
def print_looser():
    print("""
 ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄  ▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░▌
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌▐░▌          ▐░▌     ▐░▌   ▀  ▀ 
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌  ▄  ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀  ▀
    """)


# Function to display the current scores
def display_scores(players):
    print("Current Scores:")
    print("-" * 15)
    for player in players:
        print(f"{player.get_name()}: {player.get_score()} points (Total: {player.get_total_score()} points)")
    print("\n" + "-" * 15 + "\n")


# Function to select a random player to start the game
def select_starting_player(players):
    return players[random.randint(0, 1)]


# Function to update the current player
def update_current_player(players, current_player):
    if players.index(current_player) == 0:
        return players[1]
    else:
        return players[0]


# Cheat code
def cheat(player):
    print("\n" + "-" * 20 + "\nWhat would you like to change?")
    print("[1] Total score")
    print("[2] Number of turns")
    choice = input("> ")
    value = int(input("Set the new value: "))
    if choice == '1':
        player.set_total_score(value)
    elif choice == '2':
        player.set_turns(value)


# Function to play the game
def play_game(players, computer_difficulty):
    current_player = select_starting_player(players)
    print(f"\nLet's begin the game! {current_player.get_name()} starts.\n")

    dice = Dice()
    highscore = Highscore()

    while current_player.is_not_winner():
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
                    print("Oops! You rolled a 1. Your turn is over, and you\
                        scored nothing.")
                    current_player.reset_score()
                    current_player = update_current_player(players, current_player)
                else:
                    print(f"You rolled a {dice_value}!")
                    current_player.add_score(dice_value)
            elif player_choice == 'h':
                current_player.add_turn()
                current_player.update_total_score()
                current_player.reset_score()
                current_player = update_current_player(players, current_player)
            elif player_choice == 'n':
                name = input("Write your NEW name: ")
                current_player.change_name(name)
            elif player_choice == 'x':
                return
            elif player_choice == 'cheat':
                cheat(current_player)
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
                # In the following 4 lines I fixed a zero division error, not in a beautiful way,
                # but without changing too much code.
                if current_player.get_score() != 0:
                    turns_remaining = (100 - current_player.get_total_score()) // current_player.get_score()
                else:
                    turns_remaining = 5

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
                current_player = update_current_player(players, current_player)

    # Game ends, determine the weener and update high scores
    print(f"\n{current_player.get_name()} wins with a score of {current_player.get_total_score() + current_player.get_score()} points!")
    if current_player.is_human():
        print_weener()
        highscore.update_high_scores(current_player.get_name(), current_player.get_turns())
        input()
    else:
        print_looser()
